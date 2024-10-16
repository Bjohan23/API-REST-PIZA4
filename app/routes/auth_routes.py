from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from app.models.Usuarios import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    contrasena = request.json.get('contrasena', None)

    user = Usuario.get_or_none(Usuario.username == username)
    if user and user.verify_password(contrasena):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Nombre de usuario o contraseña incorrectos"}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        usuario = Usuario.create_user(
            username=data['username'],
            contrasena=data['contrasena'],
            nombre=data['nombre'],
            telefono=data['telefono'],
            direccion=data['direccion'],
            email=data['email'],
            dni=data['dni']
        )
        return jsonify(usuario.to_dict()), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "Esta es una ruta protegida"}), 200