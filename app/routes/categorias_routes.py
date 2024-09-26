from flask import Blueprint, request, jsonify
from app.services.services_categorias import (
    get_all_categorias,
    get_categoria_by_id,    
    create_categoria,
    update_categoria_by_id,
    delete_categoria_by_id
)

categorias_bp = Blueprint('categorias', __name__)

@categorias_bp.route('/', methods=['GET'])
def get_categorias():
    return get_all_categorias()

@categorias_bp.route('/<int:categoria_id>', methods=['GET'])
def get_categoria(categoria_id):
    return get_categoria_by_id(categoria_id)

@categorias_bp.route('/', methods=['POST'])
def post_categoria():
    data = request.json
    return create_categoria(data)

@categorias_bp.route('/<int:categoria_id>', methods=['PUT'])
def update_categoria(categoria_id):
    data = request.json
    return update_categoria_by_id(categoria_id, data)

@categorias_bp.route('/<int:categoria_id>', methods=['DELETE'])
def delete_categoria(categoria_id):
    return delete_categoria_by_id(categoria_id)
