# swagger/swagger_definitions.py
from flasgger import swag_from

def get_list_companies_swagger():
    return swag_from({
        'parameters': [
            {
                'name': 'offset',
                'in': 'query',
                'type': 'integer',
                'required': False,
                'description': 'Número de registros a serem pulados (offset)',
                'default': 0
            },
            {
                'name': 'limit',
                'in': 'query',
                'type': 'integer',
                'required': False,
                'description': 'Número de registros a serem retornados por página',
                'default': 20
            },
            {
                'name': 'sort',
                'in': 'query',
                'type': 'string',
                'required': False,
                'description': 'Campo pelo qual ordenar os resultados',
                'default': 'created_at'
            },
            {
                'name': 'dir',
                'in': 'query',
                'type': 'string',
                'required': False,
                'description': "Direção da ordenação ('asc' ou 'desc')",
                'default': 'asc'
            }
        ],
        'responses': {
            200: {
                'description': 'Lista de empresas com paginação',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'total_companies': {'type': 'integer'},
                        'total_pages': {'type': 'integer'},
                        'current_page': {'type': 'integer'},
                        'empresas': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'cnpj': {'type': 'string'},
                                    'register_name': {'type': 'string'},
                                    'business_name': {'type': 'string'},
                                    'cnae': {'type': 'string'},
                                    'created_at': {'type': 'string', 'format': 'date-time'},
                                    'deleted_at': {'type': 'string', 'format': 'date-time'},
                                }
                            }
                        }
                    }
                }
            },
            400: {'description': 'Erro de validação nos parâmetros'}
        }
    })

def company_details_swagger():
    return swag_from({
        'parameters': [
            {
                'name': 'cnpj',
                'type': 'string',
                'required': True,
                'in': 'query',
                'description': 'CNPJ da empresa a ser buscada'
            }
        ],
        'responses': {
            200: {
                'description': 'Detalhes da empresa',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'cnpj': {'type': 'string'},
                        'register_name': {'type': 'string'},
                        'business_name': {'type': 'string'},
                        'cnae': {'type': 'string'},
                        'created_at': {'type': 'string', 'format': 'date-time'},
                        'deleted_at': {'type': 'string', 'format': 'date-time'},
                    }
                }
            },
            404: {'description': 'Empresa não encontrada'}
        }
})

def get_add_company_swagger():
    return swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'cnpj': {'type': 'string'},
                        'register_name': {'type': 'string'},
                        'business_name': {'type': 'string'},
                        'cnae': {'type': 'string'}
                    },
                    'required': ['cnpj', 'register_name', 'business_name', 'cnae']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Empresa criada com sucesso',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'cnpj': {'type': 'string'},
                        'register_name': {'type': 'string'},
                        'business_name': {'type': 'string'},
                        'cnae': {'type': 'string'},
                        'created_at': {'type': 'string', 'format': 'date-time'},
                        'deleted_at': {'type': 'string', 'format': 'date-time'},
                    }
                }
            },
            400: {'description': 'Erro ao criar a empresa'}
        }
    })

def get_modify_company_swagger():
  return swag_from({
        'parameters': [
            {
                'name': 'cnpj',
                'in': 'path',
                'type': 'string',
                'required': True,
                'description': 'CNPJ da empresa a ser atualizada'
            },
            {
                'name': 'body',
                'in': 'body',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'business_name': {'type': 'string'},
                        'cnae': {'type': 'string'}
                    },
                    'required': ['business_name', 'cnae']
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Empresa atualizada com sucesso',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'cnpj': {'type': 'string'},
                        'register_name': {'type': 'string'},
                        'business_name': {'type': 'string'},
                        'cnae': {'type': 'string'},
                        'created_at': {'type': 'string', 'format': 'date-time'},
                        'deleted_at': {'type': 'string', 'format': 'date-time'},
                    }
                }
            },
            404: {'description': 'Empresa não encontrada'}
        }
    })

def get_remove_company_swagger():
    return swag_from({
        'parameters': [
            {
                'name': 'cnpj',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': ' CNPJ da empresa a ser removida'
            }
        ],
        'responses': {
            204: {'description': 'Empresa excluída com sucesso'},
            404: {'description': 'Empresa não encontrada'}
        }
    })