from GoogleMapsUtility import GoogleMapsUtility
from best_first import Best_First


"""
python3
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
        if answer == 'n':
            # to break the while loop
            user_in = True
        elif answer != 'n':
            print("Only enter yes or no")

    print(Best_First(point_list[0], hit_list, "distance"))
    print(Best_First(point_list[0], hit_list, "time"))

if __name__ =="__main__":
    main()
