from flask import Blueprint, request, jsonify
from app.services.services_pisos import (
    get_all_pisos,
    get_piso_by_id,    
    create_piso,
    update_piso_by_id,
    delete_piso_by_id
)


pisos_bp = Blueprint('piso', __name__)

@pisos_bp.route('/', methods=['GET'])
def get_pisos():
    return get_all_pisos()

@pisos_bp.route('/<int:piso_id>', methods=['GET'])
def get_piso(piso_id):
    return get_piso_by_id(piso_id)

@pisos_bp.route('/', methods=['POST'])
def post_piso():
    data = request.json
    return create_piso(data)

@pisos_bp.route('/<int:piso_id>', methods=['PUT'])
def update_piso(piso_id):
    data = request.json
    return update_piso_by_id(piso_id, data)

@pisos_bp.route('/<int:piso_id>', methods=['DELETE'])
def delete_piso(piso_id):
    return delete_piso_by_id(piso_id)

