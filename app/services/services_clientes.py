from app.models.Personas import Persona
from flask import jsonify


def get_all_personas():
    personas = list(Persona.select().dicts())
    return jsonify(personas)

def get_persona_by_id(persona_id):
    persona = Persona.get_or_none(Persona.id == persona_id)
    if persona:
        return jsonify(persona.__data__)
    return jsonify({'message': 'Persona not found'}), 404

def create_persona(data):
    try:
        persona = Persona.create(**data)
        return jsonify(persona.__data__), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    

def update_persona_by_id(persona_id, data):
    persona = Persona.get_or_none(Persona.id == persona_id)
    if persona:
        for key, value in data.items():
            setattr(persona, key, value)
        persona.save()
        return jsonify(persona.__data__)
    return jsonify({'message': 'Persona no encontrada'}), 404

def delete_persona_by_id(persona_id):
    persona = Persona.get_or_none(Persona.id == persona_id)
    if persona:
        persona.delete_instance()
        return jsonify({'message': 'Persona eliminada correctamente '})
    return jsonify({'message': 'Persona no encontrada'}), 404

