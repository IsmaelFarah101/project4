from travel_db import Restaurant
from peewee import *

db = SqliteDatabase('travel.db')

db.connect()
##create the database tables and connect to database
def create_table():
    with db:
        db.create_tables([Restaurant])

def show():
    ##return all items in database
    try:
        return Restaurant.select()
    except Exception as e:
        print(e)
##adding new item database
def add(name,location,price,rating):
    try:
        newRestaurant = Restaurant(name=name, location=location, price=price, rating=rating)
        newRestaurant.save()
    except Exception as e:
        print(e) 
