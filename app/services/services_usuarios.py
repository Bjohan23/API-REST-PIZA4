from app.models.Usuarios import Usuario
from app.models.Personas import Persona
from flask import jsonify, request
from peewee import IntegrityError

def get_all_usuarios():
    usuarios = Usuario.select()
    return jsonify([usuario.to_dict() for usuario in usuarios]) 

def get_usuario_by_id(usuario_id):
    try:
        usuario = Usuario.get_by_id(usuario_id)
        return jsonify(usuario.to_dict())
    except Usuario.DoesNotExist:
        return jsonify({"message": "Usuario no encontrado"}), 404

def create_usuario(data):
    try:
        # Hashear la contraseña antes de crear el usuario
        contrasena_hashed = Usuario.set_password(data['contrasena'])
        usuario = Usuario.create(
            persona_id=data['persona_id'],
            contrasena=contrasena_hashed
        )
        return jsonify(usuario.to_dict()), 201
    except IntegrityError as e:
        return jsonify({"message": "Error al crear el usuario: Usuario ya existe o campos inválidos"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 400

def update_usuario_by_id(usuario_id, data):
    try:
        usuario = Usuario.get_by_id(usuario_id)

        # Actualizar campos, incluyendo el hasheo de la nueva contraseña si es proporcionada
        if 'contrasena' in data:
            usuario.contrasena = Usuario.set_password(data['contrasena'])

        if 'persona_id' in data:
            usuario.persona_id = data['persona_id']
        usuario.save()

        return jsonify(usuario.to_dict())
    except Usuario.DoesNotExist:
        return jsonify({"message": "Usuario no encontrado"}), 404
    except IntegrityError as e:
        return jsonify({"message": "Error de integridad al actualizar el usuario"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 400

def delete_usuario_by_id(usuario_id):
    try:
        usuario = Usuario.get_by_id(usuario_id)
        usuario.delete_instance()
        return jsonify({"message": "Usuario eliminado"})
    except Usuario.DoesNotExist:
        return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400
