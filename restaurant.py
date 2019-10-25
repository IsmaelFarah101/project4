from travel_db import Restaurant
from peewee import *

db = SqliteDatabase('travel.db')
db.connect()
##create the database tables and connect to database
def create_table():
    with db:
        db.create_tables([Restaurant])

def show_all_restaurant():
    try:
        data =  Restaurant.get()
        for restaurant in data:
                print(restaurant)

    except Exception as e:
        print("couldn't show all restaurant")
        
##adding new item database
def add_restaurant(name,location,price,rating):
    try:
        newRestaurant = Restaurant(name=name, location=location, price=price, rating=rating)
        newRestaurant.save()
    except Exception as e:
        print(e) 

db.close()