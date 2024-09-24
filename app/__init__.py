from flask import Flask
from app.routes.user_routes import user_bp
from app.database import database
from app.models.user import User

def create_app():
    """
    Función que crea e inicializa la aplicación Flask.
    Returns:
        Flask: La instancia de la aplicación Flask.
    """
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__)
    # Cargar la configuración de la aplicación desde el módulo 'config.Config'
    app.config.from_object('config.Config')

    # Registrar el blueprint de las rutas de usuario con el prefijo '/users'
    app.register_blueprint(user_bp, url_prefix='/users')

    # Definir la función que se ejecutará antes de cada solicitud
    @app.before_request
    def before_request():
        """
        Función que se ejecuta antes de cada solicitud.
        Se encarga de conectarse a la base de datos.
        """
        database.connect()

    # Definir la función que se ejecutará después de cada solicitud
    @app.after_request
    def after_request(response):
        """
        Función que se ejecuta después de cada solicitud.
        Se encarga de cerrar la conexión a la base de datos y devolver la respuesta.

        Args:
            response (flask.Response): La respuesta de la solicitud.

        Returns:
            flask.Response: La respuesta de la solicitud.
        """
        database.close()
        return response

    # Definir un comando de línea de comandos para inicializar la base de datos
    @app.cli.command("init-db")
    def init_db():
        """
        Función que inicializa la base de datos.
        Se conecta a la base de datos, crea la tabla 'Users' si no existe y luego cierra la conexión.
        """
        database.connect()
        print("Database initialization completed.")

    return app