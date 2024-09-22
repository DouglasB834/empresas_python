from flask import Blueprint 
from swagger.swagger_definitions import (
    company_details_swagger, 
    get_add_company_swagger, 
    get_list_companies_swagger, 
    get_modify_company_swagger, 
    get_remove_company_swagger
)

from services.company_services import (
    list_companies,
    get_company,
    create_company,
    update_company,
    delete_company
)

company_bp = Blueprint('company', __name__)

@company_bp.route('/companies', methods=["GET"])
@get_list_companies_swagger()
def companies():
    return list_companies()

@company_bp.route('/company/', methods=["GET"])
@company_details_swagger()
def company_details():
    return get_company()

@company_bp.route('/company', methods=["POST"])
@get_add_company_swagger()
def add_company():
    return create_company()

@company_bp.route('/company/<string:cnpj>', methods=["PATCH"])
@get_modify_company_swagger()
def modify_company(cnpj):
    return update_company(cnpj)

@company_bp.route('/company/<string:cnpj>', methods=['DELETE'])
@get_remove_company_swagger()
def delete_company_route(cnpj):
    return delete_company(cnpj) 
