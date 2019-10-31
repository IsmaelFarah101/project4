from unittest import TestCase
from peewee import *
import event_class
import restaurant_class
from travel_db import Restaurant
import event
import restaurant

test_db_url = SqliteDatabase('test_restaurant_travel.db')

MODELS = [Restaurant]

class BaseTestCase(TestCase):
    def setUp(self):
        test_db_url.bind(MODELS)

        test_db_url.connect()
        test_db_url.create_tables(MODELS)
    
    def tearDown(self):
        test_db_url.drop_tables(MODELS)

        test_db_url.close()
    
    def test_add_event(self):
        restaurant.add_restaurant("Restaurant Name", "Restaurant Location", "45", "2")
        
        self.compare_db_to_expected("Restaurant Name", "Restaurant Location", "45", "2")
    
    def compare_db_to_expected(self, expected_name, expected_location, expected_rating, expected_price):

        restaurant_data = Restaurant.select()
        for restaurant in restaurant_data:
            self.assertEqual(restaurant.name, expected_name)
            self.assertEqual(restaurant.location, expected_location)
            self.assertEqual(restaurant.rating, expected_rating)
            self.assertEqual(restaurant.price, expected_price)