from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.services_clientes import (
    get_all_clientes,
    get_cliente_by_id,    
    create_cliente,
    update_cliente_by_id,
    delete_cliente_by_id
)

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/', methods=['GET'])
@jwt_required()
def get_clientes():
    return get_all_clientes()

@clientes_bp.route('/<int:clientes_id>', methods=['GET'])
@jwt_required()
def get_cliente(clientes_id):
    return get_cliente_by_id(clientes_id)

@clientes_bp.route('/', methods=['POST'])
@jwt_required()
def post_cliente():
    data = request.json
    return create_cliente(data)

@clientes_bp.route('/<int:clientes_id>', methods=['PUT'])
@jwt_required()
def update_cliente(cliente_id):
    data = request.json
    return update_cliente_by_id(cliente_id, data)

@clientes_bp.route('/<int:clientes_id>', methods=['DELETE'])
@jwt_required()
def delete_cliente(cliente_id):
    return delete_cliente_by_id(cliente_id)
