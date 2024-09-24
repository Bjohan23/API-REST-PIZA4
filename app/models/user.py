from peewee import Model, AutoField, CharField, DateTimeField
from app.database import database
import datetime

class User(Model):
    id = AutoField()
    username = CharField(unique=True)
    email = CharField(index=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        table_name = 'Users'
