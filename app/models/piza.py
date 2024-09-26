from peewee import *
from datetime import datetime
from app.database import database
class BaseModel(Model):
    class Meta:
        database = database

class Persona(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=15)
    direccion = TextField()
    email = CharField(max_length=255)
    dni = CharField(max_length=10)

class Usuario(BaseModel):
    id = AutoField()
    persona = ForeignKeyField(Persona, backref='usuarios')
    contrasena = CharField(max_length=255)

class Cliente(BaseModel):
    id = AutoField()
    persona = ForeignKeyField(Persona, backref='clientes')

class Categoria(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)

class Presentacion(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    descripcion = TextField()

class Producto(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    descripcion = TextField()
    precio = DecimalField(max_digits=10, decimal_places=2)
    disponible = BooleanField()
    categoria = ForeignKeyField(Categoria, backref='productos')
    presentacion = ForeignKeyField(Presentacion, backref='productos')

class Sede(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    direccion = TextField()

class Piso(BaseModel):
    id = AutoField()
    sede = ForeignKeyField(Sede, backref='pisos')
    nombre = CharField(max_length=100)

class Mesa(BaseModel):
    id = AutoField()
    piso = ForeignKeyField(Piso, backref='mesas')
    numero = IntegerField()
    capacidad = IntegerField()
    estado = CharField(max_length=255)

class Rol(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=50)

class ListRol(BaseModel):
    id = AutoField()
    usuario = ForeignKeyField(Usuario, backref='list_roles')
    rol = ForeignKeyField(Rol, backref='list_roles')
    fecha_inicio = DateTimeField()
    fecha_fin = DateTimeField(null=True)

class PedidosComanda(BaseModel):
    id = AutoField()
    usuario = ForeignKeyField(Usuario, backref='pedidos')
    cliente = ForeignKeyField(Cliente, backref='pedidos')
    mesa = ForeignKeyField(Mesa, backref='pedidos')
    fecha = DateTimeField(default=datetime.now)
    estado = CharField(max_length=255)
    total = DecimalField(max_digits=10, decimal_places=2)

class DetallePedido(BaseModel):
    id = AutoField()
    pedido = ForeignKeyField(PedidosComanda, backref='detalles')
    producto = ForeignKeyField(Producto, backref='detalles_pedido')
    cantidad = IntegerField()
    precio = DecimalField(max_digits=10, decimal_places=2)
    descripcion = TextField(null=True)

class ComprobanteVenta(BaseModel):
    id = AutoField()
    pedido = ForeignKeyField(PedidosComanda, backref='comprobantes')
    tipo = CharField(max_length=50)
    monto = DecimalField(max_digits=10, decimal_places=2)
    fecha = DateTimeField(default=datetime.now)

def create_tables():
    with database:
        database.create_tables([Persona, Usuario, Cliente, Categoria, Presentacion, Producto, Sede, Piso, Mesa, Rol, ListRol, PedidosComanda, DetallePedido, ComprobanteVenta])

if __name__ == '__main__':
    create_tables()