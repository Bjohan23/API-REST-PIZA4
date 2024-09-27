from app.models.comprobanteVenta import ComprobanteVenta
from app.models.DetallesPedido import DetallePedido
from app.models.PedidosComanda import PedidoComanda
from app.models.Productos import Producto
from app.models.Personas import Persona
from app.models.clientes import Cliente
from app.models.Usuarios import Usuario
from app.models.PedidosComanda import Mesa
from datetime import datetime
from flask import jsonify
def get_all_comprobantes_venta():
    comprobantes = ComprobanteVenta.select()
    return [comprobante.to_dict() for comprobante in comprobantes]

def get_comprobante_venta_by_id(comprobante_id):
    try:
        comprobante = ComprobanteVenta.get(ComprobanteVenta.id == comprobante_id)
        return comprobante.to_dict()
    except ComprobanteVenta.DoesNotExist:
        return None

def create_comprobante_venta(data):
    comprobante = ComprobanteVenta.create(
        pedido_id=data['pedido_id'],
        tipo=data['tipo'],
        monto=data['monto']
    )
    return comprobante.to_dict()

def update_comprobante_venta(comprobante_id, data):
    try:
        comprobante = ComprobanteVenta.get(ComprobanteVenta.id == comprobante_id)
        comprobante.pedido_id = data.get('pedido_id', comprobante.pedido_id)
        comprobante.tipo = data.get('tipo', comprobante.tipo)
        comprobante.monto = data.get('monto', comprobante.monto)
        comprobante.save()
        return comprobante.to_dict()
    except ComprobanteVenta.DoesNotExist:
        return None

def delete_comprobante_venta(comprobante_id):
    try:
        comprobante = ComprobanteVenta.get(ComprobanteVenta.id == comprobante_id)
        comprobante.delete_instance()
        return True
    except ComprobanteVenta.DoesNotExist:
        return False

def get_comprobante_venta_detalles(comprobante_id):
    comprobante = ComprobanteVenta.get_or_none(ComprobanteVenta.id == comprobante_id)
    if comprobante:
        detalles_pedido = (DetallePedido
                           .select(DetallePedido, PedidoComanda, Producto, Cliente, Usuario, Mesa, Persona.alias('persona_cliente'), Persona.alias('persona_usuario'))
                           .join(PedidoComanda)
                           .switch(DetallePedido)
                           .join(Producto)
                           .switch(PedidoComanda)
                           .join(Cliente)
                           .join(Persona.alias('persona_cliente'), on=(Cliente.persona == Persona.alias('persona_cliente').id))
                           .switch(PedidoComanda)
                           .join(Usuario)
                           .join(Persona.alias('persona_usuario'), on=(Usuario.persona_id == Persona.alias('persona_usuario').id))
                           .switch(PedidoComanda)
                           .join(Mesa)
                           .where(PedidoComanda.id == comprobante.pedido_id.id))
        
        detalles = [detalle_pedido_to_dict(detalle) for detalle in detalles_pedido]
        comprobante_dict = {
            'id': comprobante.id,
            'pedido_id': comprobante.pedido_id.id,
            'tipo': comprobante.tipo,
            'monto': str(comprobante.monto),
            'fecha': comprobante.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'detalles_pedido': detalles
        }
        return jsonify(comprobante_dict)
    return jsonify({'error': 'Comprobante no encontrado'}), 404

def detalle_pedido_to_dict(detalle):
    return {
        'id': detalle.id,
        'pedido_id': detalle.pedido_id.id,
        'producto_id': detalle.producto_id.id,
        'producto_nombre': detalle.producto_id.nombre,
        'cantidad': detalle.cantidad,
        'precio': str(detalle.precio),
        'subtotal': str(detalle.subtotal),
        'cliente': {
            'id': detalle.pedido_id.cliente_id.id,
            'nombre': detalle.pedido_id.cliente_id.persona_cliente.nombre,
            'apellido': detalle.pedido_id.cliente_id.persona_cliente.apellido
        },
        'usuario': {
            'id': detalle.pedido_id.usuario_id.id,
            'nombre': detalle.pedido_id.usuario_id.persona_usuario.nombre,
            'apellido': detalle.pedido_id.usuario_id.persona_usuario.apellido
        },
        'mesa': {
            'id': detalle.pedido_id.mesa_id.id,
            'numero': detalle.pedido_id.mesa_id.numero
        }
    }