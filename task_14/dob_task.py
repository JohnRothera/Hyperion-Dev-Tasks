import re

# Set variables to add contents from the sample .txt file.
name = "Name \n"
birthdate = "Birthdate \n"

# Open the .txt file, iterate over it with a for loop line by line.
with open ('./DOB.txt', 'r') as file:
    for line in file: 
        
        # Use regular expressions when reading the file.
        # The first group captures non-digit characters (name).
        # The second groupd captures digits and the rest of the line (birthdate).
        match = re.search(r'(\D+)(\d.*)', line)
        
        if match:
            # Concatenate each line with a "\n". 
            name += match.group(1) + "\n"
            birthdate += match.group(2) + "\n"

# Print the results.
print(name)
print(birthdate)
