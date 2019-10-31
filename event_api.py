import requests
import os
import requests_cache
from event_class import * 

##caching requests
requests_cache.install_cache()

def getEventData(location,keyword):
    try:
        # Create the environment variable and import the event key
        event_key = os.environ.get('EVENT_KEY')
        
        # Fetch data from the eventful api
        url = 'http://api.eventful.com/json/events/search?'
        params = {'keyword:' : keyword, 'location' : location, 'page_size' : 5, 'app_key' : event_key}
        data = requests.get(url, params=params).json()
        return data['events']['event']
    except Exception as e:
        print(e)
# Create getEvents function to fetch the needed data for events info
def getEvents(location, keyword):
    try:
        # List for event data
        event_list = []
        #get api data
        events = getEventData(location,keyword)
        # Event header
        print(f'\n --EVENT INFORMATION IN {location.upper()}-- \n')

        # Add the needed data for the event info to be displayed
        for event in events:
            name = event['title']
            place = event['venue_name']
            address = event['venue_address']
            date = event['start_time']
            event_data = EventData(name, place, address, date)
            event_list.append(event_data) # Add the needed data to the event_list
            print(event_data)

        # Return the list of classes
        return event_list

    except Exception as e:
        print('Please enter valid event city name')
        print(e)