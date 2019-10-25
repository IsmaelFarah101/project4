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