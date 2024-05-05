"""
Load the price of a product and the quantity to carry.
Show how much should be paid an integer value is entered in the product price 
"""
""" 
product_quantity = int(input("Enter the products for buying: "))
product_price = int(input("Enter the price of the product: "))
amount_pay = product_quantity * product_price
print(f"the total amount to pay for client is: {amount_pay}")
"""
class Product:
    def __init__(self):
        self.product_price= int(input("Enter the price of the product: "))
        self.product_quantity= int(input("Enter the quantity of the product: "))
        
    def calculate_product(self):
        return self.product_price * self.product_quantity
    
product = Product()
amount_pay = product.calculate_product()
print(f"The total amount to be pay is: {amount_pay}")