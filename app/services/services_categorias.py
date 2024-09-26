from app.models.Productos import  Categoria
from flask import jsonify


def get_all_categorias():
    categorias = list(Categoria.select().dicts())
    return jsonify(categorias)

def get_categoria_by_id(categoria_id):
    categoria = Categoria.get_or_none(Categoria.id == categoria_id)
    if categoria:
        return jsonify(categoria.__data__)
    return jsonify({'message': 'Categoria not found'}), 404

def create_categoria(data):
    try:
        categoria = Categoria.create(**data)
        return jsonify(categoria.__data__), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
def update_categoria_by_id(categoria_id, data):
    categoria = Categoria.get_or_none(Categoria.id == categoria_id)
    if categoria:
        for key, value in data.items():
            setattr(categoria, key, value)
        categoria.save()
        return jsonify(categoria.__data__)
    return jsonify({'message': 'Categoria no encontrada'}), 404

def delete_categoria_by_id(categoria_id):
    categoria = Categoria.get_or_none(Categoria.id == categoria_id)
    if categoria:
        categoria.delete_instance()
        return jsonify({'message': 'categoria eliminada correctamente'})
    return jsonify({'message': 'Categoria not found'}), 404
