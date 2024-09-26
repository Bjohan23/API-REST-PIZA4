from .DetallesPedido import DetallePedido
from .PedidosComanda import PedidoComanda
from  .Usuarios import Usuario
from .Productos import Producto
from .Personas import Persona

# Si añades más modelos en el futuro, puedes importarlos aquí
# from .other_model import OtherModel

# Esto hace que sea más fácil importar todos los modelos en otros lugares de tu aplicación
__all__ = ['Usuario', 'Producto', 'Persona', 'DetallePedido', 'PedidoComanda']