from peewee import Model, AutoField, ForeignKeyField, DateTimeField, DecimalField, CharField, IntegerField
from app.database import database
from app.models.PedidosComanda import PedidoComanda
from app.models.Productos import Producto
import datetime

class DetallePedido(Model):
    id = AutoField()
    pedido = ForeignKeyField(PedidoComanda, backref='detallespedido', on_delete='CASCADE')
    producto = ForeignKeyField(Producto, backref='detallespedido', on_delete='CASCADE')
    cantidad = IntegerField()
    precio = DecimalField(max_digits=10, decimal_places=2)
    descripcion = CharField()

    class Meta:
        database = database
        table_name = 'detallespedido'

    def to_dict(self):
        return {
            'id': self.id,
            'pedido': self.pedido.to_dict(),
            'producto': self.producto.to_dict(),
            'cantidad': self.cantidad,
            'precio': str(self.precio),
            'descripcion': self.descripcion
        }