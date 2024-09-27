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
        # Crear la persona primero
        persona_data = {
            'nombre': data['nombre'],
            'telefono': data['telefono'],
            'direccion': data['direccion'],
            'email': data['email'],
            'dni': data['dni']
        }
        persona = Persona.create(**persona_data)

        # Hashear la contraseña antes de crear el usuario
        contrasena_hashed = Usuario.set_password(data['contrasena'])
        usuario = Usuario.create(
            persona_id=persona.id,
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
        persona = usuario.persona_id  # Obtener la persona asociada

        # Actualizar campos del usuario, incluyendo el hasheo de la nueva contraseña si es proporcionada
        if 'contrasena' in data and data['contrasena']:
            usuario.contrasena = Usuario.set_password(data['contrasena'])

        if 'persona_id' in data:
            usuario.persona_id = data['persona_id']

        # Actualizar campos de la persona asociada
        persona_data = ['nombre', 'telefono', 'direccion', 'email', 'dni']
        for field in persona_data:
            if field in data:
                setattr(persona, field, data[field])

        # Guardar los cambios
        usuario.save()
        persona.save()

        return jsonify(usuario.to_dict())
    except Usuario.DoesNotExist:
        return jsonify({"message": "Usuario no encontrado"}), 404
    except Persona.DoesNotExist:
        return jsonify({"message": "Persona no encontrada"}), 404
    except IntegrityError as e:
        return jsonify({"message": "Error de integridad al actualizar el usuario"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 400

def delete_usuario_by_id(usuario_id):
    try:
        usuario = Usuario.get_by_id(usuario_id)
        persona_id = usuario.persona_id.id  # Obtener la ID de la persona asociada
        # Eliminar el usuario
        usuario.delete_instance()

        # Eliminar la persona asociada
        persona = Persona.get_by_id(persona_id)
        persona.delete_instance()

        return jsonify({"message": "Usuario y persona eliminados"})
    except Usuario.DoesNotExist:
        return jsonify({"message": "Usuario no encontrado"}), 404
    except Persona.DoesNotExist:
        return jsonify({"message": "Persona no encontrada"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400
