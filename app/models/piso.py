from peewee import Model, AutoField, CharField, ForeignKeyField
from app.database import database

class Sede(Model):
    id = AutoField()
    nombre = CharField(max_length=100)
    direccion = CharField()

    class Meta:
        database = database
        table_name = 'sede'

class Piso(Model):
    id = AutoField()
    sede_id = ForeignKeyField(Sede, backref='piso', on_delete='CASCADE')
    nombre = CharField(max_length=100)

    class Meta:
        database = database
        table_name = 'piso'
