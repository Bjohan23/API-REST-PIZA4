from peewee import Model, AutoField, ForeignKeyField, DateTimeField, DecimalField, CharField
from app.database import database
from app.models.PedidosComanda import PedidoComanda
import datetime

class ComprobanteVenta(Model):
    id = AutoField()
    pedido_id = ForeignKeyField(PedidoComanda, backref='comprobantesventa', on_delete='CASCADE')
    tipo = CharField(max_length=255)
    monto = DecimalField(max_digits=10, decimal_places=2)
    fecha = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        table_name = 'comprobanteventa'

    def to_dict(self):
        return {
            'id': self.id,
            'pedido_id': self.pedido_id.id,
            'tipo': self.tipo,
            'monto': str(self.monto),
            'fecha': self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        }