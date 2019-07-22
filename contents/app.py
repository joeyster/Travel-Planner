from GoogleMapsUtility import GoogleMapsUtility


"""

USE dFS
 - choose closest city from current point and go to next


"""

def main():

    graph_data = []
    ob1 = GoogleMapsUtility()
    user_in = False
    while user_in == False:
        start_point = input("Enter starting destination: ")
        end_point = input("End destination: ")
        #start_point = 'anaheim'
        #end_point = 'chicago'
        data = ob1.directionsRequest(start_point,end_point)
        graph_data.append(data)
        print(graph_data)

        answer = input("Enter another start to end destination? y/n: ")
        if answer == 'n':
            # to break the while loop
            user_in = True
        elif answer != 'n':
            print("Only enter yes or no")

main()
