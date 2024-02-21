print("According to the amount of money you have, make an algorithm that calculates the entries that can be purchased to enter the cinema, knowing that the cost  of the general entry is $ 15 per person.")

# create variables with my balance and constans with price of the tickect of cinema.
my_balance = int(input("Enter my balance in money:$"))
tickect_price = 15

# calculate the general entry tickects
num_tickets =  my_balance // tickect_price
remaining_money = my_balance % tickect_price

# print messages of money balance 
print(f"with this money ${my_balance:.2f}, you can buy this tickects {num_tickets} for cinema") 
print(f"You will have this: ${remaining_money:.2f} after pay tickects of cinema")


