# Store the intial sentance as a string variable
sentance = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Strip the "!" from the sentance and print
print(sentance.replace("!", " "))

# Reprint the sentance all upper case and remove the exclamations again 
print(sentance.replace("!", " ").upper())

# Print the entance in reverse and remove the exclamations
print(sentance.replace("!", " ")[::-1])

# worth noting that we could have removed the exclamations and 
# stored this as a new variable to eliminate using the replace function 
# multiple times. However, I wanted to stick as closely to the brief as possible
