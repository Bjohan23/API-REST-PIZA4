from flask import Flask
from flask_jwt_extended import JWTManager
from app.routes.productos import productos_bp
from app.routes.auth_routes import auth_bp
from app.database import database
from app.routes.usuarios_routes import usuarios_bp
from app.routes.categorias_routes import categorias_bp
from app.routes.cliente_routes import clientes_bp
from app.routes.piso_routes import pisos_bp
from app.routes.mesa_routes import mesas_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Configurar Flask-JWT-Extended
    app.config["JWT_SECRET_KEY"] = "scrypt:32768:8:1$G7poecr8n85E8NT1$ce0a5df4a97bfb20af97d81f3947b5d76baa2e3683a83a513849624f46e4f6414dedaa42feae6d4651f2133e6c9cd1091cf8a5faf60318819890b55849140629"  # Cambia esto por una clave secreta segura
    jwt = JWTManager(app)

    # Registrar los blueprints de rutas
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(categorias_bp, url_prefix='/categorias')
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(pisos_bp, url_prefix='/piso')
    app.register_blueprint(mesas_bp, url_prefix='/mesas')

    @app.before_request
    def before_request():
        database.connect()

    @app.after_request
    def after_request(response):
        database.close()
        return response

    return app