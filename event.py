from travel_db import Event
from peewee import *

db = SqliteDatabase('travel.db')

db.connect()
##create the database tables and connect to database
def create_table():
    with db:
        db.create_tables([Event])

def show_event(name):
    ##return all items in database
    try:
        return Event.get(Event.name == name)
    except Exception as e:
        print(e)
    
    db.close()

def show_all_event():
    try:
        return Event.get()
    except Exception as e:
        print(e)
##adding new item database
def add_event(name, place, address, date):
    try:
        newEvent = Event(name=name, place=place, address=address, date=date)
        newEvent.save()
    except Exception as e:
        print(e)
    
    db.close()
