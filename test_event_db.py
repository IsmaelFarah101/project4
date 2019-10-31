from unittest import TestCase
from peewee import *
import event_class
import restaurant_class
from travel_db import Event
import event
import restaurant
from unittest.mock import patch

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
        
        self.compare_add_event_test("Concert Name", "Concert Place", "Concert Address","10/31/2019 00:00:00")
    
    def test_show_event(self):
        event.add_event("Concert Name", "Concert Place", "Concert Address", "10/31/2019 00:00:00")
        self.compare_show_event_test()
    
    @patch('builtins.print')
    def compare_show_event_test(self, expected_display):
        event.show_all_event()
        expected_display.assert_called_once_with("Concert Name")

    def compare_add_event_test(self, expected_name, expected_place, expected_address, expected_date):

        event_data = Event.select()
        for event in event_data:
            self.assertEqual(event.name, expected_name)
            self.assertEqual(event.place, expected_place)
            self.assertEqual(event.address, expected_address)
            self.assertEqual(event.date, expected_date)

        
    


