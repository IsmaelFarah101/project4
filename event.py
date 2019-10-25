from travel_db import Event
from peewee import *

db = SqliteDatabase('travel.db')

db.connect()

def create_table():
    with db:
        db.create_tables([Event])

def show_event():
    try:
        return Event.select()
    except Exception as e:
        print(e)
    
    db.close()

def add_event(name, place, address, date):
    try:
        newEvent = Event(name=name, place=place, address=address, date=date)
        newEvent.save()
    except Exception as e:
        print(e)
    
    db.close()
