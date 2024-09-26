from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.security import hash_password

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = list(User.select().dicts())
    return jsonify(users)

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        return jsonify(user.__data__)
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    try:
        user = User.create(**data)
        return jsonify(user.__data__), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.get_or_none(User.id == user_id)
    if user:
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return jsonify(user.__data__)
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        user.delete_instance()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404