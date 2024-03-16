"""
# Carry up the loads of 2 whole numbers on the keyboard and print your sum and your product. 
number_one = int(input("Enter the firts number: "))
number_two = int(input("Enter the second number: "))
numbers_sum = number_one + number_two
numbers_prod = number_one * number_two
print(f"The sum of the numbers is: {numbers_sum} and the multiplication of the numbers is: {numbers_prod} ")
"""
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

"""
# Convert app in oop 
class Whole_numbers:
    def __init__(self):
        # initialize constructor method to initialize the whole numbers object with numbers  
        self.num1 = 0
        self.num2 = 0
        self.sum_result = 0
        self.product_result = 0

        
    # Creating method to enter inputs    
    def get_inputs(self):
        self.number_one     = int(input("Enter the first number: ")) 
        self.number_two     = int(input("Enter the second number: ")) 
    # Method for calculate the sum of the two numbers    
    def calculate_sum(self):
        self.sum_result = self.number_one + self.number_two
    # Method for calculate the product of the two numbers
    def calculate_product(self):
        self.product_result = self.number_one * self.number_two
    # Method for display results 
    def display_results(self):
        print(f"The result of the sum is: {self.sum_result} and result of the multiplication is {self.product_result}")
# instance objects
def main():
    whole_numbers = Whole_numbers()
    whole_numbers.get_inputs()
    whole_numbers.calculate_sum()
    whole_numbers.calculate_product()
    whole_numbers.display_results()
if __name__ =="__main__":
    main()