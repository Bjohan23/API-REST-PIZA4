from app.models.DetallesPedido import DetallePedido
from app.models.PedidosComanda import PedidoComanda
from app.models.Productos import Producto
from app.models.Personas import Persona
from app.models.clientes import Cliente
from app.models.Usuarios import Usuario
from app.models.PedidosComanda import Mesa
from datetime import datetime
from flask import jsonify
from peewee import JOIN , fn

def get_all_detalles_pedido():
    PersonaCliente = Persona.alias()
    PersonaUsuario = Persona.alias()

    detalles_pedido = (DetallePedido
                       .select(DetallePedido, PedidoComanda, Producto, Cliente, Usuario, Mesa, PersonaCliente, PersonaUsuario)
                       .join(PedidoComanda)
                       .switch(DetallePedido)
                       .join(Producto)
                       .switch(PedidoComanda)
                       .join(Cliente)
                       .join(PersonaCliente, on=(Cliente.persona == PersonaCliente.id))
                       .switch(PedidoComanda)
                       .join(Usuario)
                       .join(PersonaUsuario, on=(Usuario.persona_id == PersonaUsuario.id))
                       .switch(PedidoComanda)
                       .join(Mesa))
    
    return jsonify([detalle_pedido_to_dict(detalle) for detalle in detalles_pedido])


def get_detalle_pedido_by_id(detalle_pedido_id):
    PersonaCliente = Persona.alias()
    PersonaUsuario = Persona.alias()

    detalle_pedido = (DetallePedido
                      .select(DetallePedido, PedidoComanda, Producto, Cliente, Usuario, Mesa, PersonaCliente, PersonaUsuario)
                      .join(PedidoComanda)
                      .switch(DetallePedido)
                      .join(Producto)
                      .switch(PedidoComanda)
                      .join(Cliente)
                      .join(PersonaCliente, on=(Cliente.persona == PersonaCliente.id))
                      .switch(PedidoComanda)
                      .join(Usuario)
                      .join(PersonaUsuario, on=(Usuario.persona_id == PersonaUsuario.id))
                      .switch(PedidoComanda)
                      .join(Mesa)
                      .where(DetallePedido.id == detalle_pedido_id)
                      .get_or_none())
    
    if detalle_pedido:
        return jsonify(detalle_pedido_to_dict(detalle_pedido))
    return jsonify({'message': 'Detalle de pedido no encontrado'}), 404

def detalle_pedido_to_dict(detalle):
    fecha = detalle.pedido.fecha
    if isinstance(fecha, str):
        fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S') 
    return {
        'id': detalle.id,
        'pedido': {
            'id': detalle.pedido.id,
            'estado': detalle.pedido.estado,
            'fecha': detalle.pedido.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'total': str(detalle.pedido.total),
            'cliente': {
                'id': detalle.pedido.cliente_id.id,
                'nombre': detalle.pedido.cliente_id.persona.nombre,
                'telefono': detalle.pedido.cliente_id.persona.telefono,
                'email': detalle.pedido.cliente_id.persona.email,
            },
            'usuario': {
                'id': detalle.pedido.usuario_id.id,
                'nombre': detalle.pedido.usuario_id.persona_id.nombre,
            },
            'mesa': {
                'id': detalle.pedido.mesa_id_id,
                'numero': detalle.pedido.mesa_id.numero,
            },
        },
        'producto': {
            'id': detalle.producto.id,
            'nombre': detalle.producto.nombre,
            'descripcion': detalle.producto.descripcion,
            'precio': str(detalle.producto.precio),
            'categoria': detalle.producto.categoria.nombre,
        },
        'cantidad': detalle.cantidad,
        'precio': str(detalle.precio),
        'descripcion': detalle.descripcion,
    }

def create_detalle_pedido(data):
    try:
        detalle_pedido = DetallePedido.create(**data)
        return jsonify(detalle_pedido.to_dict()), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

def update_detalle_pedido_by_id(detalle_pedido_id, data):
    detalle_pedido = DetallePedido.get_or_none(DetallePedido.id == detalle_pedido_id)
    if detalle_pedido:
        for key, value in data.items():
            setattr(detalle_pedido, key, value)
        detalle_pedido.save()
        return jsonify(detalle_pedido.to_dict())
    return jsonify({'message': 'Detalle de pedido no encontrado'}), 404

def delete_detalle_pedido_by_id(detalle_pedido_id):
    detalle_pedido = DetallePedido.get_or_none(DetallePedido.id == detalle_pedido_id)
    if detalle_pedido:
        detalle_pedido.delete_instance()
        return jsonify({'message': 'Detalle de pedido eliminado exitosamente'})
    return jsonify({'message': 'Detalle de pedido no encontrado'}), 404

def get_detalles_pedido_by_pedido_id(pedido_id):
    detalles_pedido = DetallePedido.select().join(PedidoComanda).where(PedidoComanda.id == pedido_id)
    return jsonify([detalle.to_dict() for detalle in detalles_pedido])

def get_detalles_pedido_by_producto_id(producto_id):
    detalles_pedido = DetallePedido.select().join(Producto).where(Producto.id == producto_id)
    return jsonify([detalle.to_dict() for detalle in detalles_pedido])