##
# API KEY AIzaSyAY1aatbdVCglJhXI0HFddm5pEkPTUpBFU
# python3.6
# importing required libraries
import requests, json

api_key ='AIzaSyAlFOfYJqGZR3a_5VcbrihyaproXXWTeY4'

class GoogleMapsUtility():
    def __init__(self,api_key,start_point,end_point):
        self.apikey = api_key
        self.start_point = start_point
        self.end_point = end_point


    def directionsRequest(self):
        # url variable store url
        url ='https://maps.googleapis.com/maps/api/directions/json'
        # Get method of requests module
        payload = {'key':api_key,'origin':self.start_point,'destination':self.end_point}
        # makes google directions API requests
        response = requests.get(url,params=payload)
        # grabs JSON object from API request
        data = response.json()
        # checks if the status is successful
        if response.status_code == 200:
            # iterates throught the JSON object
            for directions in data['routes'][0]['legs']:
                # gets distance dictionary from json
                distance = directions['distance']
                # gets duration dictionary from json
                duration = directions['duration']
                # get the value from distance
                distance_miles = distance.get("text")
                # get the value from duration
                duration_hours = duration.get("text")
                return int(distance_miles.rstrip(" mi").replace(",", "")), duration_hours
        elif response.status_code != 200:
            print(response.status_code)
            print(response.json())


        #duration hours later implement if have time