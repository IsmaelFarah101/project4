from travel_db import Event
from peewee import *

db = SqliteDatabase('travel.db')

db.connect()
##create the database tables and connect to database
def create_table():
    with db:
        db.create_tables([Event])

def show_event():
    ##return all items in database
    try:
        return Event.select()
    except Exception as e:
        print(e)
    
    db.close()
##adding new item database
def add_event(name, place, address, date):
    try:
        newEvent = Event(name=name, place=place, address=address, date=date)
        newEvent.save()
    except Exception as e:
        print(e)
    
    db.close()
