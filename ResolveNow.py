print("Find the surface area of a square knowing the value of one side")
try:
    side_length = int(input("Enter the side length of the surface area: "))
    surface_area = side_length * side_length
    print(f"The surface area of the square is: {surface_area}")
except ValueError:
    print("Invalid input, Please enter a valid integer")
print("Carry up the loads of 2 whole numbers on the keyboard and print your sum and your product")
try:
    number_one = int(input("Enter the firts number: "))
    number_two = int(input("Enter the second number: "))
    numbers_sum = number_one + number_two
    numbers_prod = number_one * number_two
    print(f"The sum of the numbers is: {numbers_sum} and the multiplication of the numbers is: {numbers_prod} ")
except ValueError:
    print("Invalid input, Please enter a valid integer")
print("Load the price of a product and the quantity to carry.Show how much should be paid an integer value is entered in the product price.")
try: 
    product_quantity = int(input("Enter the products for buying: "))
    product_price = int(input("Enter the price of the product: "))
    amount_pay = product_quantity * product_price
    print(f"the total amount to pay for client is: {amount_pay}")
except ValueError:
    print("Invalid input, Please enter a valid integer")
print("Carrying the side of a square side, show the screen perimeter thereof the perimeter of a square is calculated by multiplying the value of the side by four")
try:
    side_length_two = int(input("Enter side length of the perimeter: "))
    perimeter_square = side_length_two * 4
    print(f"The perimeter of square is {perimeter_square}")
except ValueError:
    print("Invalid input, Please enter a valid integer")    
print(" Write a program in which four numbers are enter, calculate and inform the sum of the first two and the product of the third and the fourth.")
try:
    number_onee = int(input("Enter the first number "))
    number_twoo = int (input("Enter the second number "))
    number_three = int (input("Enter the third number "))
    number_fourth = int (input("Enter the fourth number "))
    sum_first_numbers = number_onee + number_twoo
    product_seconds_numbers = number_three * number_fourth
    print(f"the sum of the two first number is {sum_first_numbers} and the product of two seconds numbers is {product_seconds_numbers} ")
    
except ValueError:
    print("Invalid input, Please enter a value integer")
print(" Perform a program that reads four numerical values and inform your sum and average.")   
try:
    num_one = int(input("Enter the first number "))
    num_two = int(input("Enter the second number "))
    num_three = int(input("Enter the third number "))
    num_fourh = int(input("Enter the fourth number ")) 
    average_nums = num_one + num_two + number_three + num_fourh / 4
    print(f"The average of the four numbers is {average_nums}")

except ValueError:
    print("Invalid input, Please enter a value integer")
print("Calculate the monthly salary of an operator knowing the number of hours worked and the value per hour.")
try:
    worked_hour = int(input("Enter hours worked "))
    value_hour  = int(input("Enter value per hour "))
    monthly_salary = worked_hour * value_hour
    print(f"The salary monthly of the operator is {monthly_salary} ")
     
except ValueError:
    print("Invalid input, Please enter a value integer")
    
print(" Write a program that asks the user for their weight (in kg) and height (in meters), calculates the body mass index and stores it in a variable, and displays on the screen the sentence where is the calculated body mass index rounded Tu índice de masa corporal es <imc>with <imc>two decimals.")

weight_person = int(input("Enter weight of the person "))
height_person = float(input("Enter height of the person "))
imc_person = weight_person * (height_person)**2
print(f"The index mass of the person is {imc_person}")

print("Write a program that asks the user for an amount to invest, the annual interest and the number of years, and displays on the screen the capital obtained from the investment.")

amount_invest = int(input("Enter the amount invest for the user "))
annual_interest = int(input("Enter the annual interest for the user "))
years_numbers = int(input("Enter numbers of years "))
# I need formula for compound interest
capital_obtained = amount_invest * (1 + annual_interest/100)**years_numbers
print(f"The capital obtained is {capital_obtained}")

print("A toy store is very successful in two of its products: clowns and dolls. They usually sell by mail and the logistics company charges them by weight of each package, so they must calculate the weight of the clowns and dolls that will appear in each package on demand. Each clown weighs 112 g and each doll 75 g. Write a program that reads the number of clowns and dolls sold in the last order and calculates the total weight of the package that will be shipped.")
CLOWNS_WEIGHT = 112
DOLLS_WEIGHT = 75
clowns_numbers = int(input("Enter numbers of clowns for package "))
dolls_numbers = int(input("Enters numbers of dolls for package "))
package_weight = (clowns_numbers *CLOWNS_WEIGHT) + (dolls_numbers * DOLLS_WEIGHT)
print(f"The total weight of the package is {package_weight}") 

print("Imagine that you have just opened a new savings account that offers you 4% interest per year. These savings due to interest, which are not collected until the end of the year, are added to the final balance of your savings account. Write a program that begins by reading the amount of money deposited in the savings account, entered by the user. Then the program must calculate and display on the screen the amount of savings after the first, second and third years. Round each amount to two decimal places.")
INTEREST_PER_YEARD = 4
amount_deposited = int(input("Enter old amount deposited in the account: "))
years_numbers = int(input("Enter numbers of years: "))
total_interest_per_firts_year = amount_deposited * (INTEREST_PER_YEARD / 100)
total_interest_per_years = (total_interest_per_firts_year)**years_numbers
print(f"Total interest per years is {total_interest_per_years} and the interest per one year is {total_interest_per_firts_year}")

