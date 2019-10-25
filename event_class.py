class EventData:
    
    def __init__(self, name, place, address, date):
        self.name = name
        self.place = place
        self.address = address
        self.date = date

    def __str__(self):
        return f'Name: {self.name} | Place: {self.place} | Address: {self.address} | Date: {self.date} \n'