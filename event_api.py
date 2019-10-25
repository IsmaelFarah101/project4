import requests
import os

# Create event class to safe all the objects
class EventData:
    
    def __init__(self, name, place, address, date):
        self.name = name
        self.place = place
        self.address = address
        self.date = date

    def __str__(self):
        return f'Name: {self.name} | Place: {self.place} | Address: {self.address} | Date: {self.date} \n'

def getEvents(location, keyword):

    try:
        # Create the environment variable
        event_key = os.environ.get('EVENT_KEY')
        
        # Fetch data from the eventful api
        url = 'http://api.eventful.com/json/events/search?'
        params = {'keyword:' : keyword, 'location' : location, 'page_size' : 5, 'app_key' : event_key}
        data = requests.get(url, params=params).json()

        events_data = data['events']['event']

        event_list = []

        print(f'\n --EVENT INFORMATION IN {location}-- \n')

        for event in events_data:
            name = event['title']
            place = event['venue_name']
            address = event['venue_address']
            date = event['start_time']
            event_data = EventData(name, place, address, date)
            event_list.append(event_data) # Add the needed data to the event_list
            print(event_data)

        return event_list

    except Exception as e:
        raise e