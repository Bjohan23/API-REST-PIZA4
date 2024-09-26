from flask import Blueprint, request, jsonify
from app.models.Productos import Producto, Categoria, Presentacion
from app.utils.security import hash_password

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['GET'])
def get_productos():
    productos = list(Producto.select().dicts())
    return jsonify(productos)

@productos_bp.route('/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
        producto = Producto.get_or_none(Producto.id == producto_id)
        if producto:
            return jsonify(producto.__data__)
        return jsonify({'message': 'Producto not found'}), 404

@productos_bp.route('/', methods=['POST'])
def post_producto():
    data = request.json
    try:
        producto = Producto.create(**data)
        return jsonify(producto.__data__), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
@productos_bp.route('/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    data = request.json
    producto = Producto.get_or_none(Producto.id == producto_id)
    if producto:
        for key, value in data.items():
            setattr(producto, key, value)
        producto.save()
        return jsonify(producto.__data__)
    return jsonify({'message': 'Producto not found'}), 404

@productos_bp.route('/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    producto = Producto.get_or_none(Producto.id == producto_id)
    if producto:
        producto.delete_instance()
        return jsonify({'message': 'Producto deleted successfully'})
    return jsonify({'message': 'Producto not found'}), 404