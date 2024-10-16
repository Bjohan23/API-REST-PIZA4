from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.services_mesas import (
    get_all_mesas,
    get_mesa_by_id,
    create_mesa,
    update_mesa_by_id,
    delete_mesa_by_id,
    get_mesas_by_piso_id,
    get_mesas_by_piso_id_and_estado,
    get_mesas_by_estado
)


mesas_bp = Blueprint('mesas', __name__)

@mesas_bp.route('/', methods=['GET'])
@jwt_required()
def get_mesas():
    return get_all_mesas()

@mesas_bp.route('/<int:mesa_id>', methods=['GET'])
@jwt_required()
def get_mesa(mesa_id):
    return get_mesa_by_id(mesa_id)

@mesas_bp.route('/', methods=['POST'])
@jwt_required()
def post_mesa():
    data = request.json
    return create_mesa(data)

@mesas_bp.route('/mesas/<int:mesa_id>', methods=['PUT'])
@jwt_required()
def update_mesa(mesa_id):
    data = request.json
    return update_mesa_by_id(mesa_id, data)

@mesas_bp.route('/mesas/<int:mesa_id>', methods=['DELETE'])
@jwt_required()
def delete_mesa(mesa_id):
    return delete_mesa_by_id(mesa_id)

@mesas_bp.route('/piso/<int:piso_id>', methods=['GET'])
@jwt_required()
def get_mesas_by_piso(piso_id):
    return get_mesas_by_piso_id(piso_id)

@mesas_bp.route('/piso/<int:piso_id>/estado/<estado>', methods=['GET'])#/mesas/piso/2/estado/libre
@jwt_required()
def get_mesas_by_piso_and_estado(piso_id, estado):
    return get_mesas_by_piso_id_and_estado(piso_id, estado)

@mesas_bp.route('/estado/<string:estado>', methods=['GET'])
@jwt_required()
def get_mesas_by_estado_route(estado):
    return get_mesas_by_estado(estado)