from .usuarios_routes import usuarios_bp  # Cambiado de user_bp a usuarios_bp
from .auth_routes import auth_bp
from .productos import productos_bp
from .categorias_routes import categorias_bp

# Si añades más blueprints en el futuro, puedes importarlos aquí
# from .other_routes import other_bp

# Esto hace que sea más fácil importar todos los blueprints en app/__init__.py

__all__ = ['usuarios_bp', 'auth_bp', 'productos_bp', 'categorias_bp']  # Cambiado de user_bp a usuarios_bp