from peewee import *
import sqlite3

db = SqliteDatabase('travel.db')

class Restaurant(Model):
    name = CharField()
    location: CharField()
    price = CharField()
    rating = FloatField()

    class Meta:
        database = db

class Event(Model):
    name = CharField()
    place = CharField()
    address = CharField()
    date = DateField()

    class Meta:
        database = db
