try:
    side_length = int(input("Enter the side length of the surface area: "))
    surface_area = side_length * side_length
    print(f"The surface area of the square is: {surface_area}")
except ValueError:
    print("Invalid input, Please enter a valid integer")
print("Other exercises---------------------------------------")
try:
    number_one = int(input("Enter the firts number: "))
    number_two = int(input("Enter the second number: "))
    numbers_sum = number_one + number_two
    numbers_prod = number_one * number_two
    print(f"The sum of the numbers is: {numbers_sum} and the multiplication of the numbers is: {numbers_prod} ")
except ValueError:
    print("Invalid input, Please enter a valid integer")
print("Other exercises---------------------------------------")
try: 
    product_quantity = int(input("Enter the products for buying: "))
    product_price = int(input("Enter the price of the product: "))
    amount_pay = product_quantity * product_price
    print(f"the total amount to pay for client is: {amount_pay}")
except ValueError:
    print("Invalid input, Please enter a valid integer")
print("Other exercises---------------------------------------")
# side_length_two = int("Enter side length of the perimeter")