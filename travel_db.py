from peewee import *
import sqlite3

# Create database to be connected
db = SqliteDatabase('travel.db')

# Create database class for restaurant
class Restaurant(Model):
    name = CharField()
    location: CharField()
    price = CharField()
    rating = FloatField()

    class Meta:
        database = db

# Create database class for event
class Event(Model):
    name = CharField()
    place = CharField()
    address = CharField()
    date = DateField()

    class Meta:
        database = db
