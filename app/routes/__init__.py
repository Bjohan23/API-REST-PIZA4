from .user_routes import user_bp

# Si añades más blueprints en el futuro, puedes importarlos aquí
# from .other_routes import other_bp

# Esto hace que sea más fácil importar todos los blueprints en app/__init__.py
__all__ = ['user_bp']