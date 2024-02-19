print("Write a program that asks the user for an amount to invest, the annual interest and the number of years, and displays on the screen the capital obtained from the investment.")

amount_invest = int(input("Enter the amount invest for the user "))
annual_interest = int(input("Enter the annual interest for the user "))
years_numbers = int(input("Enter numbers of years "))
# I need formula for compound interest
capital_obtained = amount_invest * (1 + annual_interest/100)**years_numbers
print(f"The capital obtained is {capital_obtained}")
