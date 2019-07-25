from GoogleMapsUtility import GoogleMapsUtility
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


    point_list = []
    user_in = False
    while user_in == False:
        start_point = input("Enter destination (City/State): ")

        point_list.append(start_point)
        hit_list = point_list[1:len(point_list)]

        #print(point_list)
        #print(hit_list)

        answer = input("Enter another destination? y/n: ")
        if answer == 'n' or answer =='no':
            # to break the while loop
            user_in = True
        elif answer == 'y' or answer =='yes':
            user_in = False
        elif answer != 'n' or answer != 'no':
            print("Only enter yes or no")

    print(Best_First(point_list[0], hit_list, "distance"))
    print(Best_First(point_list[0], hit_list, "time"))

if __name__ =="__main__":
    main()
