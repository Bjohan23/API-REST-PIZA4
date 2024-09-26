from peewee import Model, AutoField, CharField, DateTimeField
from app.database import database
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(Model):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()
    email = CharField(index=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        table_name = 'Users'
        
    @classmethod
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)