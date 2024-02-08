original_string = (
    "Power isn't determined by your size, "
    "but by the size of your dreams!"
)

# Initialise a new empty string to store the modified characters.
pirate_string = ""

# Use a for loop to iterate over the characters in the string.
for index, char in enumerate(original_string):
    if index % 2 == 0:
        pirate_string += char.upper()
    else:
        pirate_string += char.lower()

print(pirate_string)

# Split the quote into seperate words.
split_string = original_string.split()
# Initialise an empty array to store the modified words.
pirate_string2 = []

# Use a for loop to iterate over the words split from the quote.
for index, word in enumerate(split_string):
    if index % 2 == 0:
        pirate_string2.append(word.lower())
    else:
        pirate_string2.append(word.upper())

# Use the join method to print the modified words.
print(" ".join(pirate_string2))
