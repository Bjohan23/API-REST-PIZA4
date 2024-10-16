from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.services_usuarios import (
    get_all_usuarios,
    get_usuario_by_id,    
    create_usuario,
    update_usuario_by_id,
    delete_usuario_by_id
)

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/', methods=['GET'])
@jwt_required()
def get_usuarios():
    return get_all_usuarios()

@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
@jwt_required()
def get_usuario(usuario_id):
    return get_usuario_by_id(usuario_id)

@usuarios_bp.route('/', methods=['POST'])
@jwt_required()
def post_usuario():
    data = request.json
    return create_usuario(data)

@usuarios_bp.route('/<int:usuario_id>', methods=['PUT'])
@jwt_required()
def update_usuario(usuario_id):
    data = request.json
    return update_usuario_by_id(usuario_id, data)

@usuarios_bp.route('/<int:usuario_id>', methods=['DELETE'])
@jwt_required()
def delete_usuario(usuario_id):
    return delete_usuario_by_id(usuario_id)
