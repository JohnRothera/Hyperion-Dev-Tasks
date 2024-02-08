# ask user to input their age
age = int(input("How old are you? "))

# begin using if statements to print different 
# reponses based on the users input

# if the users age is less than 13
if age < 13:
    print("You qualify for the kiddie discount.")
# if the users age is 21
elif age == 21:
    print("Congrats on your 21st!")
# if the users age is greater than 100
elif age > 100:
    print("Sorry, you;re dead.")
# if the users age is 65 or over
elif age >= 65:
    print("Enjoy your retirement!")
# if the users age is 40 or over
elif age >= 40:
    print("You're over the hill.")
# for any other age, the else statement will have it covered
else:
    print("Age is but a number.")