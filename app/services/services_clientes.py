from app.models.clientes import Cliente
from app.models.Personas import Persona
from flask import jsonify
from peewee import JOIN

def get_all_clientes():
    clientes = (Cliente
                .select(Cliente, Persona)
                .join(Persona)
                .dicts())
    return jsonify(list(clientes))

def get_cliente_by_id(cliente_id):
    cliente = (Cliente
               .select(Cliente, Persona)
               .join(Persona)
               .where(Cliente.id == cliente_id)
               .dicts()
               .first())
    if cliente:
        return jsonify(cliente)
    return jsonify({'message': 'Cliente no encontrado'}), 404

def create_cliente(data):
    try:
        persona_data = {
            'nombre': data.get('nombre'),
            'apellido': data.get('apellido'),
            'direccion': data.get('direccion'),
            'telefono': data.get('telefono'),
            'email': data.get('email')
        }
        persona = Persona.create(**persona_data)
        cliente = Cliente.create(persona=persona)
        return jsonify({
            'id': cliente.id,
            'persona_id': persona.id,
            'nombre': persona.nombre,
            'apellido': persona.apellido,
            'direccion': persona.direccion,
            'telefono': persona.telefono,
            'email': persona.email,
        }), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

def update_cliente_by_id(cliente_id, data):
    cliente = Cliente.get_or_none(Cliente.id == cliente_id)
    if cliente:
        persona = cliente.persona
        for key, value in data.items():
            if hasattr(persona, key):
                setattr(persona, key, value)
        persona.save()
        return jsonify({
            'id': cliente.id,
            'persona_id': persona.id,
            'nombre': persona.nombre,
            'apellido': persona.apellido,
            'direccion': persona.direccion,
            'telefono': persona.telefono,
            'email': persona.email,
        })
    return jsonify({'message': 'Cliente not found'}), 404

def delete_cliente_by_id(cliente_id):
    cliente = Cliente.get_or_none(Cliente.id == cliente_id)
    if cliente:
        cliente.delete_instance()
        return jsonify({'message': 'Cliente deleted successfully'}), 200
    return jsonify({'message': 'Cliente not found'}), 404