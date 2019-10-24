from travel_db import Restaurant
from peewee import *

db = SqliteDatabase('travel.db')

db.connect()

def create_table():
    with db:
        db.create_tables([Restaurant])

def show():
    try:
        return Restaurant.select()
    except Exception as e:
        print(e)

def add(name, location, term, price, rating):
    try:
        newRestaurant = Restaurant(name=name, location=location, term=term)
        newRestaurant.save()
    except Exception as e:
        print(e) 

def delete(name):
    try:
        Restaurant.delete().where(Restaurant.name == name).execute()
    except Exception as e:
        print(e)

def delete_all():
    try:
        Restaurant.delete().execute
    except Exception as e:
        print(e)
