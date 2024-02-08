# Initial list of items available.
menu = ["Flat White", "Croissant", "Full English", "Poached Eggs", "Toast", "Tea"]

# Dictionary to keep track of stock count using menu indexes
# as keys to account for any possible changes to the menu.
stock = {menu[0]: 170,
         menu[1]: 53,
         menu[2]: 32,
         menu[3]: 46,
         menu[4]: 72,
         menu[5]: 167
         }

# Dictionary to assign prices to items.
price = {menu[0]: 3.50,
         menu[1]: 2.80,
         menu[2]: 9.95,
         menu[3]: 5.50,
         menu[4]: 2.95,
         menu[5]: 1.95
         }

# Set an empty variable to store the total stock value. 
total_value = 0

# Iterate over the menu and calculate the value of the stock.
for item in menu:
    total_value += stock[item] * price[item]

# Print the result to two decimal places.
print(f'Total value of the menu: £{total_value:.2f}')
