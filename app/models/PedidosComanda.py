from peewee import Model, AutoField, ForeignKeyField, DateTimeField, DecimalField, CharField
from app.models.Usuarios import Usuario
from app.models.clientes import Cliente  # Asegúrate de que este modelo exista
from app.models.piso import Piso
from app.database import database
import datetime

class Mesa(Model):
    id = AutoField()
    numero = CharField(max_length=50)   
    capacidad = CharField(max_length=50)
    piso_id = ForeignKeyField(Piso, backref='mesas', on_delete='CASCADE')
    estado = CharField(max_length=50)

    class Meta:
        database = database
        table_name = 'mesas'

    def to_dict(self):
        return {
            'id': self.id,
            'piso_id': self.piso_id.id,
            'numero': self.numero,
            'estado': self.estado,
            'capacidad': self.capacidad
        }

class PedidoComanda(Model):
    id = AutoField()
    usuario_id = ForeignKeyField(Usuario, backref='pedidoscomanda', on_delete='CASCADE')
    cliente_id = ForeignKeyField(Cliente, backref='pedidoscomanda', on_delete='CASCADE')
    mesa_id = ForeignKeyField(Mesa, backref='pedidoscomanda', on_delete='CASCADE')
    fecha = DateTimeField(default=datetime.datetime.now)
    estado = CharField(max_length=255)
    total = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = database
        table_name = 'pedidoscomanda'