"""
# Carry up the loads of 2 whole numbers on the keyboard and print your sum and your product. 
number_one = int(input("Enter the firts number: "))
number_two = int(input("Enter the second number: "))
numbers_sum = number_one + number_two
numbers_prod = number_one * number_two
print(f"The sum of the numbers is: {numbers_sum} and the multiplication of the numbers is: {numbers_prod} ")
"""
# Convert this in function 
def whole_numbers(a,b):
    sum     = a+b
    product = a*b  
    return sum,product
number_one =int(input("Enter the firts number: "))
number_two =int(input("Enter the second number: "))
sum_numbers, product_numbers = whole_numbers(number_one,number_two)
print(f"the sum of the numbers is {sum_numbers} and the product of the numbers is {product_numbers}")