# Create Event class with the needed data
class EventData:
    
    def __init__(self, name, place, address, date):
        self.name = name
        self.place = place
        self.address = address
        self.date = date

    # Printing the event information
    def __str__(self):
        return f'Name: {self.name} | Place: {self.place} | Address: {self.address} | Date: {self.date} \n'