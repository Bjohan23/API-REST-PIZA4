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
from app.routes.pedidosComanda_routes import pedidosComanda_bp
from app.routes.detallesPedido_routes import detalles_pedido_bp
from app.routes.comprobanteVenta_routes import comprobante_venta_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Configurar Flask-JWT-Extended
    app.config["JWT_SECRET_KEY"] = "segura123"  # Cambia esto por una clave secreta segura
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 21600  # 6 hora de expiración
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 60  # 1 minuto expiración
    jwt = JWTManager(app)

    # Registrar los blueprints de rutas
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(categorias_bp, url_prefix='/categorias')
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(pisos_bp, url_prefix='/piso')
    app.register_blueprint(mesas_bp, url_prefix='/mesas')
    app.register_blueprint(pedidosComanda_bp, url_prefix='/pedidosComanda')
    app.register_blueprint(detalles_pedido_bp, url_prefix='/detallesPedido')
    app.register_blueprint(comprobante_venta_bp, url_prefix='/comprobanteVenta')

    @app.before_request
    def before_request():
        database.connect()

    @app.after_request
    def after_request(response):
        database.close()
        return response

    return app