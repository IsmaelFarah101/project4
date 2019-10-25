import requests
import os
##import yelp api key
yelp_key = os.environ.get('YELP')

class RestaurantData():
    def __init__(self, name, location, restaurant_type, rating, price):
        self.name = name
        self.location = location
        self.restaurant_type = restaurant_type
        self.rating = rating
        self.price = price
    ##printing the restaurant information
    def __str__(self):
        return f'Name: {self.name} Location: {self.location} Type: {self.restaurant_type} Rating: {self.rating} Price: {self.price}\n'
        


def getRestaurants(location):
    try:
        ##query and header for yelp api sorting by rating
        headers = {'Authorization' : f'Bearer {yelp_key}'}
        params = {'location': location,
            'price': '1, 2, 3',
            'sort_by': 'rating',
            'limit':5
            }
        url = 'https://api.yelp.com/v3/businesses/search'
        data = requests.get(url, params=params, headers=headers).json()
        restaurants = data['businesses']
        restaurant_list = []

        for restaurant in restaurants:
            ##getting all the needed columns and appending it to a list
            name = restaurant['name']
            location = restaurant['location']['display_address'][0]
            restaurant_type = restaurant['categories'][0]['alias']
            price = restaurant['price']
            rating = restaurant['rating']
            restaurant_data =  RestaurantData(name, location, restaurant_type,rating,price)
            restaurant_list.append(restaurant_data)
            print(restaurant_data)
        ##returning the list of classes
        return restaurant_list
    except Exception as e:
        raise e  