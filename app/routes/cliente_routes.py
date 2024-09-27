from flask import Blueprint, request, jsonify
from app.services.services_clientes import (
    get_all_clientes,
    get_cliente_by_id,    
    create_cliente,
    update_cliente_by_id,
    delete_cliente_by_id
)

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/', methods=['GET'])
def get_clientes():
    return get_all_clientes()

@clientes_bp.route('/<int:clientes_id>', methods=['GET'])
def get_cliente(clientes_id):
    return get_cliente_by_id(clientes_id)

@clientes_bp.route('/', methods=['POST'])
def post_cliente():
    data = request.json
    return create_cliente(data)

@clientes_bp.route('/<int:clientes_id>', methods=['PUT'])
def update_cliente(cliente_id):
    data = request.json
    return update_cliente_by_id(cliente_id, data)

@clientes_bp.route('/<int:clientes_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    return delete_cliente_by_id(cliente_id)
