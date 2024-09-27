from app.models.PedidosComanda import PedidoComanda , Mesa
from flask import jsonify
from peewee import JOIN

def get_all_pedidosComanda():
    pedidosComanda = PedidoComanda.select()
    return jsonify([pedidoComanda.to_dict() for pedidoComanda in pedidosComanda])

def get_pedidoComanda_by_id(pedidoComanda_id):
    pedidoComanda = PedidoComanda.get_or_none(PedidoComanda.id == pedidoComanda_id)
    if pedidoComanda:
        return jsonify(pedidoComanda.to_dict())
    return jsonify({'message': 'PedidoComanda no encontrado'}), 404

def create_pedidoComanda(data):
    try:
        pedidoComanda = PedidoComanda.create(**data)
        return jsonify(pedidoComanda.to_dict()), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
def update_pedidoComanda_by_id(pedidoComanda_id, data):
    pedidoComanda = PedidoComanda.get_or_none(PedidoComanda.id == pedidoComanda_id)
    if pedidoComanda:
        for key, value in data.items():
            setattr(pedidoComanda, key, value)
        pedidoComanda.save()
        return jsonify(pedidoComanda.to_dict())
    return jsonify({'message': 'PedidoComanda no encontrado'}), 404

def delete_pedidoComanda_by_id(pedidoComanda_id):
    pedidoComanda = PedidoComanda.get_or_none(PedidoComanda.id == pedidoComanda_id)
    if pedidoComanda:
        pedidoComanda.delete_instance()
        return jsonify({'message': 'PedidoComanda eliminado exitosamente'})
    return jsonify({'message': 'PedidoComanda no encontrado'}), 404

def get_pedidosComanda_by_mesa_id(mesa_id):
    pedidosComanda = PedidoComanda.select().join(Mesa).where(Mesa.id == mesa_id)
    return jsonify([pedidoComanda.to_dict() for pedidoComanda in pedidosComanda])

def get_pedidosComanda_by_mesa_id_and_estado(mesa_id, estado):
    pedidosComanda = PedidoComanda.select().join(Mesa).where(Mesa.id == mesa_id, PedidoComanda.estado == estado)
    return jsonify([pedidoComanda.to_dict() for pedidoComanda in pedidosComanda])

def get_pedidosComanda_by_mesa_id_and_estado_and_usuario_id(mesa_id, estado, usuario_id):
    pedidosComanda = PedidoComanda.select().join(Mesa).where(Mesa.id == mesa_id, PedidoComanda.estado == estado, PedidoComanda.usuario_id == usuario_id)
    return jsonify([pedidoComanda.to_dict() for pedidoComanda in pedidosComanda])

def get_pedidosComanda_by_mesa_id_and_estado_and_usuario_id_and_cliente_id(mesa_id, estado, usuario_id, cliente_id):
    pedidosComanda = PedidoComanda.select().join(Mesa).where(Mesa.id == mesa_id, PedidoComanda.estado == estado, PedidoComanda.usuario_id == usuario_id, PedidoComanda.cliente_id == cliente_id)
    return jsonify([pedidoComanda.to_dict() for pedidoComanda in pedidosComanda])

def get_pedidosComanda_by_mesa_id_and_estado_and_cliente_id(mesa_id, estado, cliente_id):
    pedidosComanda = PedidoComanda.select().join(Mesa).where(Mesa.id == mesa_id, PedidoComanda.estado == estado, PedidoComanda.cliente_id == cliente_id)
    return jsonify([pedidoComanda.to_dict() for pedidoComanda in pedidosComanda])

def get_pedidosComanda_by_mesa_id_and_usuario_id(mesa_id, usuario_id):
    pedidosComanda = PedidoComanda.select().join(Mesa).where(Mesa.id == mesa_id, PedidoComanda.usuario_id == usuario_id)
    return jsonify([pedidoComanda.to_dict() for pedidoComanda in pedidosComanda])


