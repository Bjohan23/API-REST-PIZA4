from peewee import Model, AutoField, ForeignKeyField, DateTimeField, DecimalField, CharField, IntegerField
from app.database import database
from app.models.PedidosComanda import PedidoComanda  # Cambiado de PedidosComanda a PedidoComanda
from app.models.Productos import Producto
import datetime

class DetallePedido(Model):
    id = AutoField()
    pedido = ForeignKeyField(PedidoComanda, backref='detallespedido', on_delete='CASCADE')  # Cambiado de PedidosComanda a PedidoComanda
    producto = ForeignKeyField(Producto, backref='detallespedido', on_delete='CASCADE')
    cantidad = IntegerField()
    precio = DecimalField(max_digits=10, decimal_places=2)
    descripcion = CharField()

    class Meta:
        database = database
        table_name = 'detallespedido'