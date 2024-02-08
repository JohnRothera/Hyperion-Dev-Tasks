# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # First error, no parentheses around print statement (syntax error)
print("\n") # Second error, unnecessary indentation and missing parenthese (syntax error)

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24" # Unnecessary indentation of entire block, assignment operator is incorrectly 
               # 'equals to' and poor naming conventions (syntax error)

age = int(age_str) # Unable to cast due to age_str containing letters (syntax error)
print(f"I'm {age} years old.") # Need to use an f string so we can concatenate string values and integer values (syntax error)

# Variables declaring additional years and printing the total years of age
years_from_now = int("3") # String must be cast into an int to perform logic in the next step (syntax error)
total_years = age + years_from_now

print(f"The total number of years: {total_years}") # Missing parentheses and double quotes around variables, 
                                                   # bad logic, wrong use of variable name and needs to be f string
                                                   # (syntax error and logical error)

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6 # Incorrect variable usage leading to inccorect logic 
                                      # no accounting for extra 6 months in below statement (syntax and logic error)

print(f"In 3 years and 6 months, I'll be + {total_months} + months old") # No parentheses, no use of f string,
                                                                         # (syntax error)

#HINT, 330 months is the correct answer
