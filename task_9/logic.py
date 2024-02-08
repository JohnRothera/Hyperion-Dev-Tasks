birthday_cake = 8
guests = 0

while guests <= 1000:
    guests += 1
    cake_left = birthday_cake / guests
    print(f"Guest: {guests} Thanks for the cake! It's delicious! cake left: {cake_left}")
    if birthday_cake <= 0:
        print("We ran out of cake, sorry! ")
        break

# In this program I wanted a simple cake calculator that would serve up a piece
# to each new guest. When there is no cake left print the message and break the loop
# However, I purposefully used bad logic so that we set a new variable 'cake_left'
# we divide all the remaining cake between how many guests are at the party and increment
# guests by one after each loop. 
# The program should just -= 1 the birthday_cake variable to work correctly.
# We will never reach the conditions of the if statement 
# as the while loop condition will continue dividing the remaining cake into smaller pieces.
    