# This program determines the fastest route based on user input for distances and speeds.
# 2 June 2024
# CSC121 m1Lab2– Review
# Ruben Guillen

"""
Pseudocode:
1. Start
2. Define a function to determine the fastest route based on user input:
    a. Initialize variables to track the fastest route and fastest time.
    b. Set a control variable to 'y' to start the loop.
3. Enter a loop that runs as long as the control variable is 'y':
    a. Prompt the user to enter the distance of the route in miles.
    b. Validate that the distance is greater than 0. If not, prompt again.
    c. Prompt the user to enter the speed for the route in miles per hour.
    d. Validate that the speed is greater than 0. If not, prompt again.
    e. Calculate the time for the route in minutes using the formula (distance / speed) * 60.
    f. Display the calculated time for the current route.
    g. Check if the current route time is the fastest. If so, update the fastest route and fastest time.
    h. Prompt the user to decide if they wish to enter more routes.
    i. Validate the user's input for continuation ('y' for yes, 'n' for no). If invalid, prompt again.
    j. If the user inputs 'y', increment the route number and continue the loop.
    k. If the user inputs 'n', exit the loop.
4. After exiting the loop, display the fastest route and the corresponding time.
5. End
"""

def calculate_route_speed():
    fastest_route = None  # Variable to store the fastest route number
    fastest_time = float('inf')  # Initialize with a very large number to ensure any valid time will be smaller
    route_number = 1  # Start with route 1
    another_route = 'y'  # Control variable for the loop

    while another_route == 'y':
        distance = float(input(f"Enter route {route_number} distance (miles): "))
        while distance <= 0:
            print("Distance must be greater than 0. Please enter a valid distance.")
            distance = float(input(f"Enter route {route_number} distance (miles): "))

        speed = float(input(f"Enter route {route_number} speed (miles/hour): "))
        while speed <= 0:
            print("Speed must be greater than 0. Please enter a valid speed.")
            speed = float(input(f"Enter route {route_number} speed (miles/hour): "))

        # Calculate the time the route should take in minutes
        time = (distance / speed) * 60
        print(f"Time for route {route_number}: {time:.2f} minutes")

        # Check if this route is the fastest
        if time < fastest_time:
            fastest_time = time
            fastest_route = route_number

        # Ask if more routes need to be entered
        another_route = input("More routes (y/n)?: ").lower()
        while another_route not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            another_route = input("More routes (y/n)?: ").lower()
        
        if another_route == 'y':
            route_number += 1  # Increment route number for the next iteration
        
        elif another_route == 'n':
            print(f"Route {fastest_route} is fastest; {fastest_time:.0f} minutes")

if __name__ == '__main__':
    calculate_route_speed()
