print("Imagine that you have just opened a new savings account that offers you 4% interest per year. These savings due to interest, which are not collected until the end of the year, are added to the final balance of your savings account. Write a program that begins by reading the amount of money deposited in the savings account, entered by the user. Then the program must calculate and display on the screen the amount of savings after the first, second and third years. Round each amount to two decimal places.")
INTEREST_PER_YEARD = 4
# Read initial amount.  
initial_amount = float(input("Enter initial amount deposited in the account:$"))
# calculated interest for first year. 
interest_one = initial_amount * (INTEREST_PER_YEARD / 100)
balance_interest_one = initial_amount + interest_one
# calculated interest for second year.   
interest_two = balance_interest_one * (INTEREST_PER_YEARD/100)
balance_interest_two = balance_interest_one + interest_two
# calculated interest for third year.   
interest_three = balance_interest_two * (INTEREST_PER_YEARD/100)
balance_interest_three = balance_interest_two + interest_three

# View saving account after the first, second and the third year.    
print("After first year: ${:.2f}".format(balance_interest_one))
print("After second year: ${:.2f}".format(balance_interest_two))
print("After third year: ${:.2f}".format(balance_interest_three))
# improve with a repetitive structure
