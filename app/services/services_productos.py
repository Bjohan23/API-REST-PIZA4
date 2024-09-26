from app.models.Productos import Producto  , Categoria
from flask import jsonify

def get_all_productos():
    productos = list(Producto.select().dicts())
    return jsonify(productos)

def get_producto_by_id(producto_id):
    producto = Producto.get_or_none(Producto.id == producto_id)
    if producto:
        producto_data = producto.__data__
        categoria = Categoria.get_or_none(Categoria.id == producto.categoria_id)
        if categoria:
            data = {
                "descripcion": producto_data['descripcion'],
                "disponible": producto_data['disponible'],
                "id": producto_data['id'],
                "nombre": producto_data['nombre'],
                "precio": producto_data['precio'],
                "presentacion": producto_data['presentacion'],
                'categoria_id': categoria.id,
                'categoria_nombre': categoria.nombre
            }
        return jsonify(data)
    return jsonify({'message': 'Producto not found'}), 404

def create_producto(data):
    try:
        producto = Producto.create(**data)
        return jsonify(producto.__data__), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

def update_producto_by_id(producto_id, data):
    producto = Producto.get_or_none(Producto.id == producto_id)
    if producto:
        for key, value in data.items():
            setattr(producto, key, value)
        producto.save()
        return jsonify(producto.__data__)
    return jsonify({'message': 'Producto not found'}), 404

def delete_producto_by_id(producto_id):
    producto = Producto.get_or_none(Producto.id == producto_id)
    if producto:
        producto.delete_instance()
        return jsonify({'message': 'Producto deleted successfully'})
    return jsonify({'message': 'Producto not found'}), 404