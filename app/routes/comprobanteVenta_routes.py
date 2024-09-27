from flask import Blueprint, request, jsonify
from app.services.services_comprobanteventa import (
    get_all_comprobantes_venta,
    get_comprobante_venta_by_id,
    create_comprobante_venta,
    update_comprobante_venta,
    delete_comprobante_venta,
    get_comprobante_venta_detalles
)

comprobante_venta_bp = Blueprint('comprobanteVenta', __name__)

@comprobante_venta_bp.route('/', methods=['GET'])
def get_comprobantes_venta():
    comprobantes = get_all_comprobantes_venta()
    return jsonify(comprobantes), 200

@comprobante_venta_bp.route('/<int:comprobante_id>', methods=['GET'])
def get_comprobante_venta(comprobante_id):
    comprobante = get_comprobante_venta_by_id(comprobante_id)
    if comprobante:
        return jsonify(comprobante), 200
    else:
        return jsonify({'error': 'Comprobante no encontrado'}), 404

@comprobante_venta_bp.route('', methods=['POST'])
def add_comprobante_venta():
    data = request.get_json()
    comprobante = create_comprobante_venta(data)
    return jsonify(comprobante), 201

@comprobante_venta_bp.route('/<int:comprobante_id>', methods=['PUT'])
def modify_comprobante_venta(comprobante_id):
    data = request.get_json()
    comprobante = update_comprobante_venta(comprobante_id, data)
    if comprobante:
        return jsonify(comprobante), 200
    else:
        return jsonify({'error': 'Comprobante no encontrado'}), 404

@comprobante_venta_bp.route('/<int:comprobante_id>', methods=['DELETE'])
def remove_comprobante_venta(comprobante_id):
    success = delete_comprobante_venta(comprobante_id)
    if success:
        return jsonify({'message': 'Comprobante eliminado'}), 200
    else:
        return jsonify({'error': 'Comprobante no encontrado'}), 404
    
@comprobante_venta_bp.route('/<int:comprobante_id>/detalles', methods=['GET'])
def get_comprobante_venta_con_detalles(comprobante_id):
    return get_comprobante_venta_detalles(comprobante_id)