# Travel Planner
Create a list of places that you can visit and provide multiple ways to move between cities. You can take a plane, train, boat, or drive. Each method of transit provides a price and travel time. The user will provide a starting location and destination and indicate their preferences -- fastest way to reach the destination, slowest way to reach the destination, cheapest way to reach the destination, and most expensive way to reach the destination.

# Developers
1. Joey Liao
   1. Best-First search implementation
1. Rosendo Inzunza
   1. Google API implementation
1. Marzia Stanekzai
   1. documentation


# Technical implementation
test

### Compile application - recommended
1. using a virtual environment: virtual env venv
2. source venv/bin/activate
3. pip install requests
4. python3.7 app.py

# Summary
1. We will be allowing the user to enter an address where they would start.
2. Users will then add addresses that they want to travel to during their vacation.
3. We will use that information to pass an arguments to a GOOGLE MAP API request.
  1. the Google map API request will give us the miles or durations from the starting point to the other cities.
  2. we will store that information to a data structure.
4. we will use the data structure to perform a best first search to find out what the most optimal route would to travel.


# Technologies used
1. [Google API](https://developers.google.com/maps/documentation/directions/start)
2. Best First search algorithm
