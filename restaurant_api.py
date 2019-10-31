import requests
import os
from restaurant_class import *

# Create getRestaurants function to fetch the needed data for events info
def getRestaurants(location):
    try:
        # Create the environment variable and import yelp api key
        yelp_key = os.environ.get('YELP_KEY')

        # Query and header for yelp api sorting by rating
        headers = {'Authorization' : f'Bearer {yelp_key}'}
        params = {'location': location,
            'price': '1, 2, 3',
            'sort_by': 'rating',
            'limit':5
            }
        url = 'https://api.yelp.com/v3/businesses/search'
        data = requests.get(url, params=params, headers=headers).json()
        restaurants = data['businesses']

        # List for restaurant data
        restaurant_list = []

        # Restaurant header
        print("--RESTAURANT INFORMATION IN "+location.upper()+"--\n")

        # Getting all the needed columns and appending it to a list
        for restaurant in restaurants:
            name = restaurant['name']
            location = restaurant['location']['display_address'][0]
            restaurant_type = restaurant['categories'][0]['alias']
            price = restaurant['price']
            rating = restaurant['rating']
            restaurant_data =  RestaurantData(name, location, restaurant_type,rating,price)
            restaurant_list.append(restaurant_data)
            print(restaurant_data)

        # Returning the list of classes
        return restaurant_list
    except Exception as e:
        print('Please enter valid city name')