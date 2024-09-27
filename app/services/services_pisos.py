from app.models.piso import Piso , Sede
from flask import jsonify
from peewee import JOIN


def get_all_pisos():
    pisos = Piso.select()
    return jsonify([piso.to_dict() for piso in pisos])

def get_piso_by_id(piso_id):
    piso = Piso.get_or_none(Piso.id == piso_id)
    if piso:
        return jsonify(piso.to_dict())
    return jsonify({'error': 'Piso not found'}), 404

def create_piso(data):
    sede = Sede.get_or_none(Sede.id == data['sede_id'])
    if sede:
        piso = Piso.create(
            sede_id=sede,
            nombre=data['nombre'],
        )
        return jsonify(piso.to_dict()), 201
    return jsonify({'error': 'Sede not found'}), 404

def update_piso_by_id(piso_id, data):
    piso = Piso.get_or_none(Piso.id == piso_id)
    if piso:
        sede = Sede.get_or_none(Sede.id == data['sede_id'])
        if sede:
            piso.sede = sede
            piso.numero = data['numero']
            piso.capacidad = data['capacidad']
            piso.save()
            return jsonify(piso.to_dict())
        return jsonify({'error': 'Sede not found'}), 404
    return jsonify({'error': 'Piso not found'}), 404

def delete_piso_by_id(piso_id):
    piso = Piso.get_or_none(Piso.id == piso_id)
    if piso:
        piso.delete_instance()
        return jsonify({'message': 'Piso deleted'})
    return jsonify({'error': 'Piso not found'}), 404
