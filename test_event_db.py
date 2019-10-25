from peewee import *
from unittest import TestCase
from travel_db import Event
import event

test_db_url = SqliteDatabase('travel.db')

MODEL = [Event]

class TestEventDB(TestCase):
    
    def setUp(self):
        test_db_url.bind(MODEL, bind_refs=False, bind_backrefs= False)

        test_db_url.create_tables(MODEL)
    



