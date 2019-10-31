from travel_db import Restaurant
from peewee import *

# Create variable db for database
db = SqliteDatabase('travel.db')

# Connect to database
db.connect()

# Create the database tables and connect to database
def create_table():
    with db:
        db.create_tables([Restaurant])

# Show all the restaurant info
def show_all_restaurant():
    try:
       restaurants = Restaurant.select()
       for restaurant in restaurants:
               print(restaurant.name)
    except Exception as e:
        print("couldn't show all restaurant")
        
# Adding new restaurant item to the database
def add_restaurant(name,location,price,rating):
    try:
        newRestaurant = Restaurant(name=name, location=location, price=price, rating=rating)
        newRestaurant.save()
    except Exception as e:
        print(e) 

db.close()