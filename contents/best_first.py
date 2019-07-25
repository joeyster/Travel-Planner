from address import Address
from GoogleMapsUtility import GoogleMapsUtility
import heapq


# enter your api key here
api_key ='AIzaSyAlFOfYJqGZR3a_5VcbrihyaproXXWTeY4'

class Best_First():
    def __init__(self, start, hit_list, heuristic):
        self.hit_list = hit_list.copy()
        self.start = start

        self.best_distance = 0
        self.best_time = 0
        self.route = self.start
        
        self.heuristic = heuristic

        #priority queue
        self.open = []
        heapq.heapify(self.open)

        self.algorithm(Address(self.start, 0, 0))

    def __str__(self):
        if self.heuristic == "distance":
            return f"~~~~~\nbest route: {self.route}\nbest distance: {self.meters_to_miles()}\n~~~~~"
        elif self.heuristic == "time":
            return f"~~~~~\nbest route: {self.route}\nbest time: {self.seconds_to_time()}\n~~~~~"
    
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

            if self.heuristic == "distance":
                heapq.heappush(self.open, (distance, point_B))
            elif self.heuristic == "time":
                heapq.heappush(self.open, (time, point_B))

            #add children to root. key = address, value = Address
            root.children[point_B] = Address(point_B, distance, time)
        
        # print(f"self.open: {self.open}")
        popped = heapq.heappop(self.open) #(miles/time, addr)
        heuristic_value = popped[0]
        addr = popped[1]

        self.route = self.route + " -> " + addr
        self.best_distance = self.best_distance + heuristic_value
        self.best_time = self.best_time + heuristic_value

        #remove explored from list
        self.hit_list.remove(addr)

        self.algorithm(root.children[addr]) #{addr : Address()}

    def meters_to_miles(self):
        return round((self.best_distance/1000) * 0.62137)

    def seconds_to_time(self):
        # https://www.w3resource.com/python-exercises/python-basic-exercise-65.php
        time = self.best_time
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        return f"{day} days {hour} hours {minutes} minutes"