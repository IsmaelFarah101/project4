from travel_db import Event
from peewee import *

# Create variable db for database
db = SqliteDatabase('travel.db')

# Connect to database
db.connect()

# Create the database tables and connect to database
def create_table():
    with db:
        db.create_tables([Event])

# Show all the events info
def show_all_event():
    try:
        events = Event.select()
        for event in events:
            print(event.name)
    except Exception as e:
        print(e)

# Adding new event item to the database
def add_event(name, place, address, date):
    try:
        newEvent = Event(name=name, place=place, address=address, date=date)
        newEvent.save()
    except Exception as e:
        print(e)
    
    db.close()
