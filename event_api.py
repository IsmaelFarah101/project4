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
        return (f'Name: {self.name} | Place: {self.place} | Address: {self.address} | Date: {self.date}')

def main():

    try:

        # Get the location and keyword from the user
        location = user_input_location()
        keyword = user_input_keyword()

        # Create the environment variable
        event_key = os.environ.get('EVENT_KEY')
        
        # Fetch data from the eventful api
        url = 'http://api.eventful.com/json/events/search?'
        params = {'keyword:' : keyword, 'location' : location, 'app_key' : event_key}
        data = requests.get(url, params=params).json()

        events_data = data['events']['event']

        event_list = []

        for event in events_data:
            name = event['title']
            place = event['venue_name']
            address = event['venue_address']
            date = event['start_time']
            event_data = EventData(name, place, address, date)
            print(name, place, address, date)
            event_list.append(event_data) # Add the needed data to the event_list
        
        return event_list

    except Exception as e:
        raise e

def user_input_location():

    location_input = input('Enter the location for more information: ')
    return location_input

def user_input_keyword():

    keyword_input = input('Enter the keyword for the event: ')
    return keyword_input

if __name__ == '__main__':
    main()