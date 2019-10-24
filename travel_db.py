from peewee import *
import sqlite3

db = SqliteDatabase('travel.db')

class Restaurant(Model):
    name = CharField()
    location: CharField()
    term = CharField()
    price = CharField()
    rating = FloatField()

    class Meta:
        database = db

class Event(Model):
    name = CharField()
    place = CharField()
    address = CharField()
    DATA = DateField()

    class Meta:
        database = db
