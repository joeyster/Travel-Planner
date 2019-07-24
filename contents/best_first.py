from address import Address
from GoogleMapsUtility import GoogleMapsUtility
import heapq


# enter your api key here
api_key ='AIzaSyAlFOfYJqGZR3a_5VcbrihyaproXXWTeY4'

class Best_First():
    def __init__(self, start, hit_list):
        self.hit_list = hit_list 
        self.start = start

        self.best_distance = 0
        self.route = self.start

        #priority queue
        self.open = []
        heapq.heapify(self.open)

        self.algorithm(Address(self.start, 0, 0))

    def __str__(self):
        return f"~~~~~\nbest route: {self.route}\nbest distance: {self.best_distance}\n~~~~~"
    
    def algorithm(self, next_state):
        if len(self.hit_list) == 0:
            return "reached end"
        #starting at first point
        root = next_state

        for point in range(len(self.hit_list)):
            #points are addresses
            point_A = root.address
            point_B = self.hit_list[point] 

            connection = GoogleMapsUtility()
            distance, time = connection.directionsRequest(point_A, point_B)

            heapq.heappush(self.open, (distance, point_B))

            #add children to root. key = address, value = Address
            root.children[point_B] = Address(point_B, distance, time)
        
        popped = heapq.heappop(self.open) #(miles, addr)
        miles = popped[0]
        addr = popped[1]

        self.route = self.route + " -> " + addr
        self.best_distance = self.best_distance + miles

        #remove explored from list
        self.hit_list.remove(addr)

        self.algorithm(root.children[addr]) #{addr : Address()}
