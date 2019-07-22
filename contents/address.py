print("address imported")

class Address():
    def __init__(self, address, distance, time):
        #google api 
        self.address = address 
        self.distance = distance #miles 
        self.time = time #minutes

        self.children = {}

    def __str__(self):
        return "~~~~~\naddress: " + str(self.address) + "\ndistance: " + str(self.distance) + "\ntime: " + str(self.time) + "\n~~~~~"