from datetime import datetime
from flask import Flask, jsonify, request
from models import db, Empresa
from validate_docbr import CNPJ

import re

app = Flask(__name__)
app.config["SECRET_KEY"] = "COGNITO"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres.qnrmwwuiglvkgzchsmxa:G1xXYhZt9BKKWfDD@aws-0-sa-east-1.pooler.supabase.com:6543/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # sinalização" de modificaçõe, :Definir como False é uma boa prática para economizar memória
app.config['SQLALCHEMY_ECHO'] = True #consultas SQL geradas pelo SQLAlchemy sejam exibidas no console.

db.init_app(app)
with app.app_context():
    db.create_all()

# rotas e metodos

def make_response(data = None, message = None, status_code = 200):
    response = {}
    if data is not None:
        response['data'] = data
    if message is not None:
        response['message'] = message
    return jsonify(response), status_code

def validate_company_data(data):
    required_fields = ['cnpj', 'register_name', 'business_name', 'cnae']
    cnpj = data['cnpj']
    cnae = data['cnae']

    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Campo obrigatório ausente ou vazio: {field}"

    if not re.match(r'^\d{14}$', cnpj):
        return False, "CNPJ inválido. Deve conter exatamente 14 dígitos numéricos."
    
    if not re.match(r'^\d{7}$', cnae):
        return False, "CNAE inválido. Deve conter 7 dígitos numéricos."
    
    validator = CNPJ()
    if not validator.validate(cnpj):
        return False, "CNPJ inválido. O número não corresponde a um CNPJ válido."
    
    return True, None

def validate_update_data(data):
    required_fields = ['business_name', 'cnae']
    cnae = data['cnae']
    
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Campo obrigatório ausente ou vazio: {field}"

    if not re.match(r'^\d{7}$', cnae):
        return False, "CNAE inválido. Deve conter 7 dígitos numéricos."
    
    return True, None

def format_company_response(company):
    response = {
        "cnpj": company.cnpj,
        "register_name": company.register_name,
        "business_name": company.business_name,
        "cnae": company.cnae,
        "created_at":company.created_at
    }
    if company.deleted_at:
        response["deleted_at"] = company.deleted_at
    return response

@app.route('/companies', methods=["GET"])
def list_companies():

    offset = request.args.get('offset', default = 0, type = int)
    limit = request.args.get('limit', default = 20 , type = int)
    sort = request.args.get('sort', default = 'created_at', type = str) 

    dir = request.args.get('dir', default = 'asc', type = str)

    if dir not in ['asc', 'desc']:
        return make_response( message="Parâmetro 'dir' inválido. Use 'asc' ou 'desc'.", status_code = 400 )
    
    try:
        order_by = getattr(Empresa, sort)
    except AttributeError:
        return make_response(message="Campo de ordenação inválido", status_code=400)

    if dir == 'desc':
        order_by = order_by.desc()

    if sort not in ['id', 'cnpj', 'register_name', 'business_name', 'cnae', 'created_at']:
        return make_response(message="Parametro de ordenação invalido: 'sort'", status_code=400)
    
    total_companies = Empresa.query.filter_by(deleted_at=None).count()

    total_pages = (total_companies // limit) + (1 if total_companies % limit > 0 else 0)

    current_page = (offset // limit) + 1

    if offset >= total_companies or current_page > total_pages:
        return make_response(message="Página inválida. Não há mais registros.", status_code=400)


    companies = Empresa.query.filter_by(deleted_at=None).order_by(order_by).offset(offset).limit(limit).all()

    result = [format_company_response(company) for company in companies]
    
    return make_response(data={
        "total_companies": total_companies,
        "total_pages": total_pages,
        "current_page": current_page,
        "empresas": result,
    })


@app.route('/company/', methods=["GET"])
def get_company():
    try:
        cnpj = request.args.get('cnpj')
        if not cnpj:
            return make_response(message="CNPJ não fornecido.", status_code=400)

        if cnpj:
            company = Empresa.query.filter_by(cnpj=cnpj).first()

        if not company:
            return make_response(message="Empresa não encontrada", status_code = 404)
        
        result = format_company_response(company)
        return make_response(data=result, status_code=200)
    except Exception as e:
        return make_response(message=f"Erro ao buscar a empresa: {str(e)}", status_code=500)



@app.route('/company', methods=["POST"])
def create_company():
    try:
        data = request.get_json()
        is_valid, error_message = validate_company_data(data)
        
        if not is_valid:
            return make_response(message=error_message, status_code = 400)
        
        data['register_name'] = data['register_name'].lower()
        existing_company = Empresa.query.filter(
            (Empresa.cnpj == data['cnpj']) | (Empresa.register_name == data['register_name'])
        ).first()
        
        if existing_company:
            if existing_company.cnpj == data['cnpj']:
                return make_response(message="Já existe empresa com este CNPJ.", status_code=400)
            if existing_company.register_name == data['register_name']:
                return make_response(message="Já existe empresa com este nome registrado.", status_code=400)
        
        new_company = Empresa(
            cnpj=data['cnpj'],
            register_name=data['register_name'],
            business_name=data['business_name'],
            cnae=data['cnae']
        )
        db.session.add(new_company)
        db.session.commit()
        return make_response(
            data = format_company_response(new_company),
            message="Empresa registrada com sucesso",
            status_code=201
        )
    except Exception as e:
        db.session.rollback()
        return make_response(message=f"Erro ao registar empresa:{str(e)}", status_code=500)

@app.route('/company/<int:id>', methods=["PATCH"])
def update_company(id):
    try:
        data = request.get_json()
        company = Empresa.query.get(id)
        if not company:
            return jsonify({"message": "Company not found"}), 404

        is_valid, error_message = validate_update_data(data)
        if not is_valid:
            return make_response(message=error_message, status_code = 400)

        company.business_name = data.get('business_name', company.business_name)
        company.cnae = data.get('cnae', company.cnae)
        db.session.commit()
        return make_response(
            data=format_company_response(company),
            message="Empresa atualizada com sucesso"
        )
    except Exception as e:
        db.session.rollback()
        return make_response(message=f"Error ao Atualizar empresa: {str(e)}", status_code=500)

@app.route('/company/<int:id>', methods=["DELETE"])
def delete_company(id):
    try:
        company = Empresa.query.get(id)
        if not company:
            return make_response(message="Company not found", status_code=404)

        if company.deleted_at:
            return make_response(message="Empresa já está excluída", status_code=400)

        company.deleted_at = datetime.utcnow()  # Marca a data de deleção
        db.session.commit()
        return make_response(message="Empresa excluída com sucesso", status_code=204)
    except Exception as e:
        db.session.rollback()
        return make_response(message=f"Error ao excluir empresa: {str(e)}", status_code=500)

# para entender que  estamos em ambiente dev
if __name__ == "__main__":
    app.run(debug=True)
