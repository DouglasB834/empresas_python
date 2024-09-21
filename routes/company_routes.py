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

@company_bp.route('/company/<int:id>', methods=["PATCH"])
@get_modify_company_swagger()
def modify_company(id):
    return update_company(id)

@company_bp.route('/company/<int:id>', methods=["DELETE"])
@get_remove_company_swagger()
def remove_company(id):
    return delete_company(id)
