# This is a programme that will allow for user input to choose 
# a holiday destination, stay duration, car rental duration,
# and calculate overall costs. 
 
# Begin by creating a list of destinations available.
destinations = ["London", "Tokyo", "Bangkok", "New York", 
                "San Francisco", "Cape Town"]

# Create a dictionary for hotel prices based on location.
hotel_costs = {destinations[0]: 190,
               destinations[1]: 240,
               destinations[2]: 140,
               destinations[3]: 300,
               destinations[4]: 290,
               destinations[5]: 200}

# Do the same for the flight cost. Using dictionaries
# will be helpful for future scalability.
flight_costs = {destinations[0]: 420,
                destinations[1]: 890,
                destinations[2]: 480,
                destinations[3]: 560,
                destinations[4]: 730,
                destinations[5]: 600}

# Create a function that will check for user input. We only want integers 
# to be entered so we will inform the user if they have entered different.
def option_input_checker(choice):
    while True:
        try:
            return int(input(choice))
        except ValueError:
            print("Please only enter numerical values! Thank you!")

# The hotel cost function takes two inputs -  
# the stay duration and the location chosen. 
# Due to the indexing of python lists, we must remember to  
# - 1 from the users choice.
def hotel_cost(num_nights, city_flight):
    return num_nights * hotel_costs[destinations[city_flight - 1]]

# The plane_cost function works in much the same way
# but as it is a fixed cost we don't need the duration of the stay.
def plane_cost(city_flight):
    return flight_costs[destinations[city_flight - 1]]

# The car_rental function only needs an integer parameter as we have
# a fixed price in this program. Of course, we could expand on the options 
# available quite easily. For the purposes of this task, we'll keep it simple.  
def car_rental(rental_days):
    return rental_days * 80

# The holiday_cost function simply adds all the individual costs together.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

city_flight_options = list(range(1, len(destinations) + 1))

# Pesent the user with available options. 
# The use of a for loop reduces the lines of code and aids scalability.
# We don't want the first option printed to be zero indexed, hence 'start=1'.
print("Where would you like to visit on your trip?")
print("Options currently available are:")
for index, destination in enumerate(destinations, start=1):
    print(f"{index}. {destination}")

# Use a while loop to ensure the user chooses a valid option. 
while True:
    city_flight = option_input_checker("Enter the number corresponding to your chosen destination: ")
    if 1 <= city_flight <= len(destinations):
        print(f"\nThanks! You're going to {destinations[city_flight - 1]}! \n")
        break
    else:
        print("Invalid choice. Please enter a number within the available options.")

# Begin assigning variables utilising the created functions.                      
flight_total = plane_cost(city_flight)

num_nights = option_input_checker("How many nights would you like to stay? \n")
num_nights_total = hotel_cost(num_nights, city_flight)
    
rental_days = option_input_checker("How many days would you like car hire? \n")
rental_days_total = car_rental(rental_days)

# Enter the variables into our holiday_cost function.
total = holiday_cost(num_nights_total, flight_total, rental_days_total)

# Print out the results. Happy holidays!
print("Thank you for choosing to book a holiday with us! \n"
      f"The total cost of your holiday package is: ${total} \n"
      f"Hotel fee: ${num_nights_total} \n"
      f"Car Hire fee: ${rental_days_total} \n"
      f"Flight fee: ${flight_total}")
