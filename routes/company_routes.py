from flask import Blueprint, jsonify, request
from services.company_services import (
    list_companies,
    get_company,
    create_company,
    update_company,
    delete_company
)

company_bp = Blueprint('company', __name__)

@company_bp.route('/companies', methods=["GET"])
def companies():
    return list_companies()

@company_bp.route('/company/', methods=["GET"])
def company_details():
    return get_company()

@company_bp.route('/company', methods=["POST"])
def add_company():
    return create_company()

@company_bp.route('/company/<int:id>', methods=["PATCH"])
def modify_company(id):
    return update_company(id)

@company_bp.route('/company/<int:id>', methods=["DELETE"])
def remove_company(id):
    return delete_company(id)
