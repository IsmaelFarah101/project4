from weather import getWeather
from restaurant_api import getRestaurants
from event_api import getEvents
from restaurant import *
from event import *
import restaurant
import event

def main():
    restaurant.create_table()
    event.create_table()
    show_menu()

def show_menu():
    print("****Travel App****")
    menu = int(input('1. Enter 1 to Search New Events/Restaurants/Weather: \n 2. Enter 2 to Search Through Bookmarks: '))
    while True:
        if menu == 1:
            print("Enter a city and country code to see"
              " the weather, top restaurants\n and concerts")
            print("You can find country codes at https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes ")
            city, country_code, keyword = getInput()
            getWeather(city, country_code)
            restaurants = getRestaurants(city)
            events = getEvents(city, keyword)
            bookmarkQuestion = input('Do you want to save the restaurants and events(y/n)?: ')    
            break
        elif menu == 2:
            bookmark_question = input('1. Enter 1 to get all Events \n Enter 2 to search Event by name: \n Enter 3 to get all Restaurants ')
            break    
        else:
            menu = int(input('1. Enter 1 to Search New Events/Restaurants/Weather: \n 2. Enter 2 to Search Through Bookmarks: '))

    if bookmarkQuestion == 'y' or bookmarkQuestion == 'Y':
        for restaurant in restaurants:
            add_restaurant(restaurant.name, restaurant.location, restaurant.price, restaurant.rating)
        for event in events:
            add_event(event.name, event.place, event.address, event.date)
        print('Thank You')
    elif bookmarkQuestion == 'n' or bookmarkQuestion == 'N':
        print('Thank You')
    else:
        print()
def getInput():
    city = input(("City: "))
    country_code = input(("Country Code: "))
    keyword = input(("Enter keyword for event: "))
    return city, country_code, keyword
    # receiving user input
def getRestaurantName():
    name = input('Enter name of restaurant: ')
    return name
def getEventName():
    name = input('Enter name of event')
    return name
    











if __name__ == '__main__':
        main()
