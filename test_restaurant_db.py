from unittest import TestCase
from peewee import *
import event_class
import restaurant_class
from travel_db import Restaurant
import event
import restaurant
from unittest.mock import patch

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
        restaurant.add_restaurant("Restaurant Name", "Restaurant Location", "2", "45.0")
        
        self.compare_add_restaurant_test("Restaurant Name", "Restaurant Location", "2", "45.0")
    
    def test_show_restaurant(self):
        restaurant.add_restaurant("Restaurant Name", "Restaurant Location", "2", "45.0")
        self.compare_show_restaurant_test()
    
    @patch('builtins.print')
    def compare_show_restaurant_test(self, expected_display):
        restaurant.show_all_restaurant()
        expected_display.assert_called_once_with("Restaurant Name")
    
    def compare_add_restaurant_test(self, expected_name, expected_location, expected_price, expected_rating):
        
        restaurant_data = Restaurant.select()
        for restaurant in restaurant_data:
            self.assertEqual(restaurant.name, expected_name)
            self.assertEqual(restaurant.price, expected_price)
            self.assertEqual(restaurant.rating, float(expected_rating))
            