age = "36"

# Compilation error due to unclosed string
name = "John Rothera
# Correct syntax - name = "John Rothera"

# Compilation error, unable to divide the 'age' string with an int
months_age = age / 12
# Correct syntax - months_age = int(age) / 12

print("Hi, my name is ", name, "and I'm ", age, "years old") 

# Logic error, we need to multiply the age by 12 to get it in months but we have divided
print("In months, I am ", months_age)
# Correct syntax - print("In months, I am ", int(age) * 12)

# Runtime error, Zero Division error
print(int(age) / 0)
