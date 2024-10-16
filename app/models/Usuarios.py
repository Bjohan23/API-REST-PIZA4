from peewee import Model, AutoField, ForeignKeyField, CharField
from app.database import database
from app.models.Personas import Persona
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(Model):
    id = AutoField()
    persona_id = ForeignKeyField(Persona, backref='usuarios', on_delete='CASCADE')
    contrasena = CharField(max_length=255)
    username = CharField(max_length=255, unique=True)

    class Meta:
        database = database
        table_name = 'usuarios'

    @classmethod
    def create_user(cls, username, contrasena, **persona_data):
        persona = Persona.create(**persona_data)
        return cls.create(
            persona_id=persona,
            username=username,
            contrasena=generate_password_hash(contrasena)
        )

    def verify_password(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'persona_id': self.persona_id.id,
            'nombre': self.persona_id.nombre,
            'telefono': self.persona_id.telefono,
            'direccion': self.persona_id.direccion,
            'email': self.persona_id.email,
            'dni': self.persona_id.dni
        }