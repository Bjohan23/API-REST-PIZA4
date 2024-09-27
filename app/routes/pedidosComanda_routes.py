from flask import Blueprint, request, jsonify
from app.services.services_productos import (
    get_all_productos,
    get_producto_by_id,
    create_producto,
    update_producto_by_id,
    delete_producto_by_id
)
