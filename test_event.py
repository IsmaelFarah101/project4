import unittest
from unittest import TestCase
from unittest.mock import patch, call

import event_api


class TestEvent(TestCase):

    @patch('event_api.getEvents')
    def test_get_data_needed_for_events(self, mock_locations, mock_keywords):
        mock_location = 'minneapolis'
        mock_keyword = 'musics'
        example_api_response = {'keyword' : mock_keyword, 'location' : mock_location}
        
        mock_locations.side_effect = [ example_api_response ]
        mock_keywords.side_effect = [ example_api_response ]
        
        get_data = event_api.getEvents(mock_location, mock_keyword)
        
        expected_location = event_api.getEvents(mock_keyword, mock_location)

        self.assertEqual(get_data, expected_location)
       


if __name__ == '__main__':
    unittest.main()   
