from address import Address
from google_maps_api import GoogleMapsUtility


# enter your api key here
api_key ='AIzaSyAlFOfYJqGZR3a_5VcbrihyaproXXWTeY4'

class Best_First():
    def __init__(self, point_list, hit_list):
        self.start = point_list[0]
        self.end = point_list[-1]
        self.hit_list = hit_list #list of address string

        #nodes only
        self.open = []
        self.closed = []

        self.algorithm()
    
    def algorithm(self):
        #starting at first point
        root = Address(self.start, 0, 0)
        # print(f"root.children: {root.children}")

        for point in range(len(self.hit_list)):
            #points are addresses
            point_A = root.address
            point_B = self.hit_list[point] 

            connection = GoogleMapsUtility(api_key, point_A, point_B)
            distance, time = connection.directionsRequest()

            if point == 0:
                best_distance = distance
                print(f"point_B: {point_B}")
                print(f"best_distance: {best_distance}")
            elif distance < best_distance:
                best_distance = distance
                print(f"point_B: {point_B}")
                print(f"best_distance: {best_distance}")

            root.children[point_B] = Address(point_B, distance, time)

        # print(f"root.children: {root.children}")
        # print(root.children["NV"])
        # print(root.children["IL"])
        # print(root.children["NY"])