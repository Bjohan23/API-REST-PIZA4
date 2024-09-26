from peewee import Model, AutoField, ForeignKeyField, CharField
from app.database import database
from app.models.Personas import Persona
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(Model):
    id = AutoField()
    persona = ForeignKeyField(Persona, backref='usuarios', on_delete='CASCADE')
    contrasena = CharField(max_length=255)

    class Meta:
        database = database
        table_name = 'usuarios'
    
    # Métodos para hashear y verificar contraseñas
    @classmethod
    def set_password(cls, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)
