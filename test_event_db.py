from unittest import TestCase
from peewee import *
import event_class
import restaurant_class
from travel_db import Event
import event
import restaurant

test_db_url = SqliteDatabase('test_event_travel.db')

MODELS = [Event]

class BaseTestCase(TestCase):
    def setUp(self):
        test_db_url.bind(MODELS)

        test_db_url.connect()
        test_db_url.create_tables(MODELS)
    
    def tearDown(self):
        test_db_url.drop_tables(MODELS)

        test_db_url.close()
    
    def test_add_event(self):
        event.add_event("Concert Name", "Concert Place", "Concert Address", "10/31/2019 00:00:00")
        

        self.compare_db_to_expected("Concert Name", "Concert Place", "Concert Address","10/31/2019 00:00:00")
    
    def compare_db_to_expected(self, expected_name, expected_place, expected_address, expected_date):

        event_data = Event.select()
        for event in event_data:
            self.assertEqual(event.name, expected_name)
            self.assertEqual(event.place, expected_place)
            self.assertEqual(event.address, expected_address)
            self.assertEqual(event.date, expected_date)

        
    


