from peewee import *
from Testkrams.config import conf
db = SqliteDatabase('game.db')


class BaseModel(Model):
    class Meta:
        database = db

class Player(BaseModel):
    # needs to store name and emoji
    player_id       = IntegerField(unique=True)
    name            = CharField(unique=True)   # don't worry about length, sqlite doesn't care anyway
    icon            = CharField()
    role            = CharField(default="")

class Poll(BaseModel):
    channel         = IntegerField()


class KillQEntry(BaseModel):
    player_id      = ForeignKeyField(Player)

class Text(BaseModel):
    text_id        = IntegerField(unique=True)
    name           = CharField()
    text_value     = CharField()



def create_tables():
    with db:
        print("Creating database tables in {}...".format(conf['database']['filename']))
        db.create_tables([Player, Poll, KillQEntry, Text])
