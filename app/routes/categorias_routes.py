from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.services_categorias import (
    get_all_categorias,
    get_categoria_by_id,    
    create_categoria,
    update_categoria_by_id,
    delete_categoria_by_id
)

categorias_bp = Blueprint('categorias', __name__)

@categorias_bp.route('/', methods=['GET'])
@jwt_required()
def get_categorias():
    return get_all_categorias()

@categorias_bp.route('/<int:categoria_id>', methods=['GET'])
@jwt_required()
def get_categoria(categoria_id):
    return get_categoria_by_id(categoria_id)

@categorias_bp.route('/', methods=['POST'])
@jwt_required()
def post_categoria():
    data = request.json
    return create_categoria(data)

@categorias_bp.route('/<int:categoria_id>', methods=['PUT'])
@jwt_required()
def update_categoria(categoria_id):
    data = request.json
    return update_categoria_by_id(categoria_id, data)

@categorias_bp.route('/<int:categoria_id>', methods=['DELETE'])
@jwt_required()
def delete_categoria(categoria_id):
    return delete_categoria_by_id(categoria_id)
