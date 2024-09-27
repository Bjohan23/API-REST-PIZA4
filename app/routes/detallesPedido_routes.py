from flask import Blueprint, request, jsonify
from app.services.services_detallePedido import (
    get_all_detalles_pedido,
    get_detalle_pedido_by_id,
    create_detalle_pedido,
    update_detalle_pedido_by_id,
    delete_detalle_pedido_by_id,
    get_detalles_pedido_by_pedido_id,
    get_detalles_pedido_by_producto_id
)

detalles_pedido_bp = Blueprint('detallesPedido', __name__)

@detalles_pedido_bp.route('/', methods=['GET'])
def get_detalles_pedido():
    return get_all_detalles_pedido()

@detalles_pedido_bp.route('/<int:detallesPedido_id>', methods=['GET'])
def get_detalle_pedido(detallesPedido_id):
    return get_detalle_pedido_by_id(detallesPedido_id)

@detalles_pedido_bp.route('/', methods=['POST'])
def create_detalle_pedido_route():
    data = request.get_json()
    return create_detalle_pedido(data)

@detalles_pedido_bp.route('/<int:detallesPedido_id>', methods=['PUT'])
def update_detalle_pedido(detallesPedido_id):
    data = request.get_json()
    return update_detalle_pedido_by_id(detallesPedido_id, data)

@detalles_pedido_bp.route('/<int:detallesPedido_id>', methods=['DELETE'])
def delete_detalle_pedido(detallesPedido_id):
    return delete_detalle_pedido_by_id(detallesPedido_id)

@detalles_pedido_bp.route('/pedido/<int:pedido_id>', methods=['GET'])
def get_detalles_pedido_by_pedido(pedido_id):
    return get_detalles_pedido_by_pedido_id(pedido_id)

@detalles_pedido_bp.route('/producto/<int:producto_id>', methods=['GET'])
def get_detalles_pedido_by_producto(producto_id):
    return get_detalles_pedido_by_producto_id(producto_id)