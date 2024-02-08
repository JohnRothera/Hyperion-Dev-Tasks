# first define each varibale for the event via user input
swimming = int(input("What was you time in minutes for the swimming event? "))
cycling = int(input("What was your time for the cycling event? "))
running = int(input("What was your time for the running event? "))

# calculate the total of each triathlon event
total = (swimming + cycling + running)

# create an if statement to see which award if any has been achieved with the total time
if total >= 111:
    print("No award, sorry! ")
elif total >= 106 and total <= 110:
    print("You have achieved the Provincial Scroll award. ")
elif total > 100 and total < 106:
    print("You have acheieved the Provincial Half Colours award. Well done! ")
elif total <= 100:
    print("You have achieved the highest award, Provincial colours. Congratulations! ")
