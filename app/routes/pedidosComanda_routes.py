from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.services_pedidosComanda import (
    get_all_pedidosComanda,
    get_pedidoComanda_by_id,
    create_pedidoComanda,
    update_pedidoComanda_by_id,
    delete_pedidoComanda_by_id,
    get_pedidosComanda_by_mesa_id,
    get_pedidosComanda_by_mesa_id_and_estado,
    get_pedidosComanda_by_mesa_id_and_estado_and_usuario_id,
    get_pedidosComanda_by_mesa_id_and_estado_and_usuario_id_and_cliente_id,
    get_pedidosComanda_by_mesa_id_and_estado_and_cliente_id,
    get_pedidosComanda_by_estado
    )



pedidosComanda_bp = Blueprint('pedidosComanda', __name__)

@pedidosComanda_bp.route('/', methods=['GET'])
@jwt_required()
def get_pedidosComanda():
    return get_all_pedidosComanda()

@pedidosComanda_bp.route('/<int:pedidoComanda_id>', methods=['GET'])
@jwt_required()
def get_pedidoComanda(pedidoComanda_id):
    return get_pedidoComanda_by_id(pedidoComanda_id)

@pedidosComanda_bp.route('/', methods=['POST'])
@jwt_required()
def create_pedidoComanda_route():
    data = request.get_json()
    return create_pedidoComanda(data)

@pedidosComanda_bp.route('/<int:pedidoComanda_id>', methods=['PUT'])
@jwt_required()
def update_pedidoComanda(pedidoComanda_id):
    data = request.get_json()
    return update_pedidoComanda_by_id(pedidoComanda_id, data)

@pedidosComanda_bp.route('/<int:pedidoComanda_id>', methods=['DELETE'])
@jwt_required()
def delete_pedidoComanda(pedidoComanda_id):
    return delete_pedidoComanda_by_id(pedidoComanda_id)

@pedidosComanda_bp.route('/mesa/<int:mesa_id>', methods=['GET'])
@jwt_required()
def get_pedidosComanda_by_mesa(mesa_id):
    return get_pedidosComanda_by_mesa_id(mesa_id)

@pedidosComanda_bp.route('/mesa/<int:mesa_id>/estado/<string:estado>', methods=['GET'])
@jwt_required()
def get_pedidosComanda_by_mesa_and_estado(mesa_id, estado):
    return get_pedidosComanda_by_mesa_id_and_estado(mesa_id, estado)

@pedidosComanda_bp.route('/mesa/<int:mesa_id>/estado/<string:estado>/usuario/<int:usuario_id>', methods=['GET'])
@jwt_required()
def get_pedidosComanda_by_mesa_and_estado_and_usuario(mesa_id, estado, usuario_id):
    return get_pedidosComanda_by_mesa_id_and_estado_and_usuario_id(mesa_id, estado, usuario_id)

@pedidosComanda_bp.route('/mesa/<int:mesa_id>/estado/<string:estado>/usuario/<int:usuario_id>/cliente/<int:cliente_id>', methods=['GET'])
@jwt_required()
def get_pedidosComanda_by_mesa_and_estado_and_usuario_and_cliente(mesa_id, estado, usuario_id, cliente_id):
    return get_pedidosComanda_by_mesa_id_and_estado_and_usuario_id_and_cliente_id(mesa_id, estado, usuario_id, cliente_id)

@pedidosComanda_bp.route('/mesa/<int:mesa_id>/estado/<string:estado>/cliente/<int:cliente_id>', methods=['GET'])
@jwt_required()
def get_pedidosComanda_by_mesa_and_estado_and_cliente(mesa_id, estado, cliente_id):
    return get_pedidosComanda_by_mesa_id_and_estado_and_cliente_id(mesa_id, estado, cliente_id)

# pedidos por estado
@pedidosComanda_bp.route('/estado/<string:estado>', methods=['GET'])
@jwt_required()
def get_pedidosComanda_by_estado_route(estado):
    return get_pedidosComanda_by_estado(estado)
