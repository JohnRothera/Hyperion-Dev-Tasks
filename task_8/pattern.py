# Set empty string variable to iterate over and add stars
stars = ""

# initialise for loop adding stars when the range is 5 and lower 
# when above 5, start removing stars
for i in range(1,10):
    if i <= 5:
        stars = stars + "*"
        print(stars)
    elif i > 5:
        index = 10 - i
        print(stars[0:index])
