# Intialise variables to keep track of total and amount of entries
user_num = 0
input_total = 0

while True:

    # Ask user for input 
    user_input = int(input("Please enter a number, when done entering numbers, enter -1 to calculate the average "))
    # Add users selection to user_num varaible
    user_num += user_input
    # Increase total entries by 1 
    input_total += 1

    if user_input == -1:
        # Remove 1 from the 'input_total' 
        input_total -= 1
        # Add 1 to users total number to account for -1 entry that reduced 'user_num' variable by 1
        user_num += 1 
        # Do simple average calculation 
        average = float(user_num / input_total)
        print("Thank you! The average of your entered numbers is: {:.2f}".format(average))
        break


