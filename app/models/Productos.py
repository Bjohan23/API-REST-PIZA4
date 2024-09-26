from peewee import Model, AutoField, CharField, DecimalField, BooleanField, ForeignKeyField
from app.database import database

class Categoria(Model):
    id = AutoField()
    nombre = CharField(max_length=100)

    class Meta:
        database = database
        table_name = 'categoría'

class Presentacion(Model):
    id = AutoField()
    nombre = CharField(max_length=100)
    descripcion = CharField()

    class Meta:
        database = database
        table_name = 'presentacion'

class Producto(Model):
    id = AutoField()
    nombre = CharField(max_length=100)
    descripcion = CharField()
    precio = DecimalField(max_digits=10, decimal_places=2)
    disponible = BooleanField()
    categoria = ForeignKeyField(Categoria, backref='productos', on_delete='CASCADE')
    presentacion = ForeignKeyField(Presentacion, backref='productos', on_delete='CASCADE')

    class Meta:
        database = database
        table_name = 'productos'
