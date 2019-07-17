# Travel Planner
Create a list of places that you can visit and provide multiple ways to move between cities. You can take a plane, train, boat, or drive. Each method of transit provides a price and travel time. The user will provide a starting location and destination and indicate their preferences -- fastest way to reach the destination, slowest way to reach the destination, cheapest way to reach the destination, and most expensive way to reach the destination.

# Developers
1. Joey Liao
   1. Contribution 1
   1. Contribution 2
   1. Contribution ...
1. Rosendo Inzunza
   1. Contribution 1
   1. Contribution 2
   1. Contribution ...
1. **Developer 3 (role)**
   1. Contribution 1
   1. Contribution 2
   1. Contribution ...

# Technical implementation <TBD>
*Provide a general discussion on the data structures and algorithms that were used to achieve the goals of the project*
>You can make use of heuristics and a best-first search to implement this.

# Usage <TBD>
*Describe how to compile and run your program.*


# Summary
1. We will be allowing the user to enter their current major city and the major cities they want to travel to
2. We will use that information to pass an arguments to a GOOGLE MAP API request
  1. the Google map API request will give us the miles from the starting point to the other cities
  2. we will store that information to a data structure
3. we will use the data structure to perform either a DFS or BFS to find out what the most optimal route would be to travel.


# Technologies used
1. Google API
