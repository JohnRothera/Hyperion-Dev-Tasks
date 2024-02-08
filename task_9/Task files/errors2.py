# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Should be a string so needs to be in double quotes (syntax error)
animal_type = "cub"
number_of_teeth = 16

# Needs to be an f string as there are strings and ints. Also, the number_of_teeth was 
# placed in the wrong position (syntax and logic error)
full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth") 

print(full_spec) # No parentheses
