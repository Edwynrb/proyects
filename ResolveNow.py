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