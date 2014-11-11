from datetime import datetime
from peewee import *

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Upload(BaseModel):
    path = CharField()
    hash = CharField(unique=True)
    date = DateTimeField(default=datetime.now)
