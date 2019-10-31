import requests
import os
from event_class import * 
##this function interacts with the api
def getEventData(location,keyword):
    try:
         # Create the environment variable
        event_key = os.environ.get('EVENT_KEY')
        
        # Fetch data from the eventful api
        url = 'http://api.eventful.com/json/events/search?'
        params = {'keyword:' : keyword, 'location' : location, 'page_size' : 5, 'app_key' : event_key}
        data = requests.get(url, params=params).json()
        event_data = data['events']['event']
        return event_data
    except Exception as e:
        print('Error Occured')


def getEvents(location, keyword):
    try:
        event_list = []
        event_data = getEventData(location,keyword)
        print(f'\n --EVENT INFORMATION IN {location.upper()}-- \n')
        for event in event_data:
            name = event['title']
            place = event['venue_name']
            address = event['venue_address']
            date = event['start_time']
            event_class = EventData(name, place, address, date)
            event_list.append(event_class) # Add the needed data to the event_list
            print(event_class)
        return event_list

    except Exception as e:
        print('Please enter valid city name')
        print(e)

