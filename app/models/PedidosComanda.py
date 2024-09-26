from peewee import Model, AutoField, ForeignKeyField, DateTimeField, DecimalField, CharField
from app.models.Usuarios import Usuario
from app.database import database
import datetime

class Mesa(Model):
    id = AutoField()
    piso = ForeignKeyField('Piso', backref='mesas', on_delete='CASCADE')
    numero = CharField(max_length=100)
    capacidad = CharField(max_length=11)
    estado = CharField(max_length=255)

    class Meta:
        database = database
        table_name = 'mesas'

class PedidoComanda(Model):
    id = AutoField()
    usuario = ForeignKeyField(Usuario, backref='pedidoscomanda', on_delete='CASCADE')
    cliente = ForeignKeyField('Cliente', backref='pedidoscomanda', on_delete='CASCADE')
    mesa = ForeignKeyField(Mesa, backref='pedidoscomanda', on_delete='CASCADE')
    fecha = DateTimeField(default=datetime.datetime.now)
    estado = CharField(max_length=255)
    total = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = database
        table_name = 'pedidoscomanda'
