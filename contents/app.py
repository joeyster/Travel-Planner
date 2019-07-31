from google_maps_utility import GoogleMapsUtility
from best_first import Best_First

"""
python3


---------------- sample -----------------


Enter destination (City/State): seattle
Enter another destination? y/n: yes
Enter destination (City/State): anaheim
Enter another destination? y/n: y
Enter destination (City/State): chicago
Enter another destination? y/n: n
~~~~~
best route: seattle -> anaheim -> chicago
best distance: 3171
~~~~~
~~~~~
best route: seattle -> anaheim -> chicago
best time: 1 days 23 hours 17 minutes
~~~~~

"""

def main():
    answer = ""
    point_list = []
    heuristic = input("Would you like the shortest distance or fastest time? (distance or time)")
    start_point = input("Enter starting point (Address, City, or State): ")
    point_list.append(start_point)
    while answer != "-1":
        answer = input("Enter a destination (enter -1 to end): ")
        if answer != "-1":
            point_list.append(answer)  

    hit_list = point_list[1:len(point_list)]
    
    print(Best_First(point_list[0], hit_list, heuristic))


def testing_address(point_list, hit_list):
    print(Best_First(point_list[0], hit_list, "distance"))
    print(Best_First(point_list[0], hit_list, "time"))
    return True


if __name__ =="__main__":
    main()