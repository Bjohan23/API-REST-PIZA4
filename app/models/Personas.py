from peewee import Model, AutoField, CharField

from app.database import database

class Persona(Model):
    id = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=15)
    direccion = CharField()
    email = CharField(max_length=255)
    dni = CharField(max_length=10)

    class Meta:
        database = database
        table_name = 'personas'
