from app.models.DetallesPedido import DetallePedido
from app.models.PedidosComanda import PedidoComanda
from app.models.Productos import Producto
from flask import jsonify

def get_all_detalles_pedido():
    detalles_pedido = DetallePedido.select()
    return jsonify([detalle.to_dict() for detalle in detalles_pedido])

def get_detalle_pedido_by_id(detalle_pedido_id):
    detalle_pedido = DetallePedido.get_or_none(DetallePedido.id == detalle_pedido_id)
    if detalle_pedido:
        return jsonify(detalle_pedido.to_dict())
    return jsonify({'message': 'Detalle de pedido no encontrado'}), 404

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