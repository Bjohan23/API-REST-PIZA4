from flask import Flask, jsonify, request
from flask_cors import CORS
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
import logging # para registro de solicitudes http en consola (para auditoria)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app, resources={r"/*": {"origins": "*"}})
    # Configurar Flask-JWT-Extended
    app.config["JWT_SECRET_KEY"] = "clavesupersegurainhackeable"  # firma de los tokens jwt (cambiar por algo más seguro)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 21600  # 6 hora de expiración
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 60  # 1 minuto expiración
    jwt = JWTManager(app)
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"message": "El token ha expirado","error": "token_expired"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"msg": "Token inválido"}), 422
    
    @jwt.unauthorized_loader
    def missing_authorization_header_callback(error):
        return jsonify({"msg": "Falta el encabezado de autorización ( token )"}), 401

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
    # Manejador de errores 404
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(error="La URL solicitada no se encontró en el servidor . Intenté nuevamente 🤓🫵 "), 404

    @app.before_request
    def log_request_info():
        logging.info(f'Request Headers: {request.headers}')
        logging.info(f'Request Body: {request.get_data()}')
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify(error="Ocurrió un error interno en el servidor."), 500
    @app.errorhandler(403)
    def forbidden(e):
        return jsonify(error="Acceso prohibido."), 403
    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify(error="No autorizado. Por favor, inicie sesión."), 401


    return app