from peewee import Model, AutoField, CharField
from app.database import database

class Cliente(Model):
    id = AutoField()
    nombre = CharField(max_length=100)
    direccion = CharField(max_length=255)

    class Meta:
        database = database
        table_name = 'clientes'