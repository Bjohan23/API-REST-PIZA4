from app.models.PedidosComanda import PedidoComanda , Mesa
from flask import jsonify
from peewee import JOIN

def get_all_mesas():
    mesas = Mesa.select()
    return jsonify([mesa.to_dict() for mesa in mesas])

def get_mesa_by_id(mesa_id):
    mesa = Mesa.get_or_none(Mesa.id == mesa_id)
    if mesa:
        return jsonify(mesa.to_dict())
    return jsonify({'message': 'Mesa not found'}), 404

def create_mesa(data):
    try:
        mesa = Mesa.create(**data)
        return jsonify(mesa.to_dict()), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
def update_mesa_by_id(mesa_id, data):
    mesa = Mesa.get_or_none(Mesa.id == mesa_id)
    if mesa:
        for key, value in data.items():
            setattr(mesa, key, value)
        mesa.save()
        return jsonify(mesa.to_dict())
    return jsonify({'message': 'Mesa not found'}), 404

def delete_mesa_by_id(mesa_id):
    mesa = Mesa.get_or_none(Mesa.id == mesa_id)
    if mesa:
        mesa.delete_instance()
        return jsonify({'message': 'Mesa deleted'})
    return jsonify({'message': 'Mesa not found'}), 404

def get_mesas_by_piso_id(piso_id):
    mesas = Mesa.select().where(Mesa.piso_id == piso_id)
    return jsonify([mesa.to_dict() for mesa in mesas])

def get_mesas_by_piso_id_and_estado(piso_id, estado):
    mesas = Mesa.select().where(Mesa.piso_id == piso_id, Mesa.estado == estado)
    return jsonify([mesa.to_dict() for mesa in mesas])

def get_mesas_by_estado(estado):
    mesas = Mesa.select().where(Mesa.estado == estado)
    return jsonify([mesa.to_dict() for mesa in mesas])

