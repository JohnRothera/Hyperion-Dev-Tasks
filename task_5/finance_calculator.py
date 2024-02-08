import math

# Present the options the user can choose from
print("\nInvestment: to calculate the amount you'll earn on your investment")
print("Bond: to calculate the amount you'll have to pay on a home loan")

while True:
    # Retrieve the user's choice and convert it to lowercase for consistency
    choice = input("\nChoose either Investment or Bond to proceed: ").lower()

    if choice == "investment":
        # Get investment details from the user
        deposit = float(input("How much money are you depositing? £"))
        interest_rate = float(input("What is the interest rate? (%) "))
        years = int(input("How many years do you plan on investing? "))

        # Convert their choice of simple or compound to lowercase for consistency
        interest = input("Would you like to calculate 'simple' or 'compound' interest? ").lower()
        if interest == "simple":
            result = deposit * (1 + interest_rate / 100 * years)
            print("Using simple interest, your total investment would be worth £{:.2f}".format(result))
        elif interest == "compound":
            result = deposit * math.pow((1 + interest_rate / 100), years)
            print("Using compound interest, your total investment would be worth £{:.2f}".format(result))
        else:
            print("Invalid input for interest calculation. Please choose either 'simple' or 'compound'.")
            continue

    elif choice == "bond":
        # Get bond details from the user
        house_value = float(input("What is the current value of your house? £"))
        interest_rate = float(input("What is the annual interest rate? (%) "))
        months = int(input("How many months do you plan to repay over? "))

        # Calculate monthly repayment amount
        monthly_interest_rate = (interest_rate / 100) / 12
        result = (monthly_interest_rate * house_value) / (1 - math.pow(1 + monthly_interest_rate, -months))
        print("Your monthly repayments will be £{:.2f}".format(result))
    else:
        print("Invalid choice. Please enter either 'Investment' or 'Bond'.")
        continue

    break
