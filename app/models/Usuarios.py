from peewee import Model, AutoField, ForeignKeyField, CharField
from app.database import database
from app.models.Personas import Persona
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(Model):
    id = AutoField()
    persona_id = ForeignKeyField(Persona, backref='usuarios', on_delete='CASCADE')
    contrasena = CharField(max_length=255)

    class Meta:
        database = database
        table_name = 'usuarios'

    # Método para convertir el objeto en un diccionario
    def to_dict(self):
        return {
            'id': self.id,
            'persona_id': self.persona_id.id,
            'nombre': self.persona_id.nombre,
            'telefono': self.persona_id.telefono,
            'direccion': self.persona_id.direccion,
            'email': self.persona_id.email,
            'dni': self.persona_id.dni,
            'contrasena': self.contrasena
        }

    # Métodos para hashear y verificar contraseñas
    @classmethod
    def set_password(cls, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)

    # Sobrescribimos el método save() para hashear la contraseña antes de guardarla
    def save(self, *args, **kwargs):
        # Si la contraseña no está hasheada aún, la hasheamos antes de guardar
        if not self.contrasena.startswith('pbkdf2:sha256'):  # Evita hashear múltiples veces
            self.contrasena = Usuario.set_password(self.contrasena)
        super().save(*args, **kwargs)