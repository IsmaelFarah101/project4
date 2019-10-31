from weather_api import getWeather
from restaurant_api import getRestaurants
from event_api import getEvents
import restaurant
import event
from event import *
from restaurant import *

def main():

    # Create tables for restaurant and event everytime user start the program
    restaurant.create_table()
    event.create_table()

    # Call the show_menu function
    show_menu()

def show_menu():

    # Program header
    print("****Travel App****")

    # Ask the user if the user want to search for the events, restaurants, weather or bookmarks
    menu = int(input('Enter 1 to Search New Events/Restaurants/Weather: \nEnter 2 to Search Through Bookmarks:\n'))

    # 
    while True:
        
        if menu == 1:
            print("Enter a city and country code to see"
              " the weather, top restaurants\n and concerts")
            print("You can find country codes at https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes ")
            city, country_code, keyword = getInput()
            getWeather(city, country_code)
            restaurants = getRestaurants(city)
            events = getEvents(city, keyword)

            # 
            while True:
                bookmarkQuestion = input('Do you want to save the restaurants and events(y/n)?: ')    
                if bookmarkQuestion == 'y' or bookmarkQuestion == 'Y':
                    for restaurant in restaurants:
                        add_restaurant(restaurant.name, restaurant.location, restaurant.price, restaurant.rating)
                    for event in events:
                        add_event(event.name, event.place, event.address, event.date)
                    print('Thank You')
                    break
                elif bookmarkQuestion == 'n' or bookmarkQuestion == 'N':
                    print('Thank You')
                    break
                else:
                    bookmarkQuestion = input('Do you want to save the restaurants and events(y/n)?: ')
            break
        elif menu == 2:
            bookmark_question = int(input('Enter 1 to get all Events \nEnter 2 to get all Restaurants \n'))
            while True:
                if bookmark_question == 1:
                    show_all_event()
                    break
                elif bookmark_question == 2:
                    show_all_restaurant()
                    break
                bookmark_question = int(input('Enter 1 to get all Events \nEnter 2 to get all Restaurants'))
            break
                  
        else:
            menu = int(input('Enter 1 to Search New Events/Restaurants/Weather: \nEnter 2 to Search Through Bookmarks: '))
            
# User input for the city, country code, and keyword
def getInput():
    city = input(("City: "))
    country_code = input(("Country Code: "))
    keyword = input(("Enter keyword for event: "))
    return city, country_code, keyword

# User input for the name of the restaurant 
def getRestaurantName():
    name = input('Enter name of restaurant: ')
    return name
def getEventName():
    name = input('Enter name of event')
    return name
    











if __name__ == '__main__':
        main()
