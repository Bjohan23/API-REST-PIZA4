from flask import Flask
from app.routes.user_routes import user_bp
from app.database import database
from app.models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(user_bp, url_prefix='/users')

    @app.before_request
    def before_request():
        database.connect()

    @app.after_request
    def after_request(response):
        database.close()
        return response

    @app.cli.command("init-db")
    def init_db():
        database.connect()
        User.create_table_if_not_exists()
        database.close()
        print("Inicialización de la base de datos completada.")

    return app