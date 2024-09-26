from flask import Blueprint, request, jsonify
from app.services.services_clientes import (
    get_all_usuarios,
    get_usuario_by_id,    
    create_usuario,
    update_usuario_by_id,
    delete_usuario_by_id
)

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/', methods=['GET'])
def get_usuarios():
    return get_all_usuarios()

@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    return get_usuario_by_id(usuario_id)

@usuarios_bp.route('/', methods=['POST'])
def post_usuario():
    data = request.json
    return create_usuario(data)

@usuarios_bp.route('/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    data = request.json
    return update_usuario_by_id(usuario_id, data)

@usuarios_bp.route('/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    return delete_usuario_by_id(usuario_id)
