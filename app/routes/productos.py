from flask import Blueprint, request, jsonify
from app.services.services_productos import (
    get_all_productos,
    get_producto_by_id,
    create_producto,
    update_producto_by_id,
    delete_producto_by_id
)
from flask_jwt_extended import  jwt_required

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['GET'])
@jwt_required()
def get_productos():
    return get_all_productos()

@productos_bp.route('/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    return get_producto_by_id(producto_id)

@productos_bp.route('/', methods=['POST'])
def post_producto():
    data = request.json
    return create_producto(data)

@productos_bp.route('/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    data = request.json
    return update_producto_by_id(producto_id, data)

@productos_bp.route('/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    return delete_producto_by_id(producto_id)