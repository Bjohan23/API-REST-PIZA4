from peewee import Model, AutoField, CharField ,ForeignKeyField
from app.database import database
from app.models.Personas import Persona

class Cliente(Model):
    id = AutoField()
    persona = ForeignKeyField(Persona, backref='clientes')

    class Meta:
        database = database
        table_name = 'clientes'

    @classmethod
    def get_or_none(cls, *query, **kwargs):
        try:
            return cls.get(*query, **kwargs)
        except cls.DoesNotExist:
            return None