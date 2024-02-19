print("Load the price of a product and the quantity to carry.Show how much should be paid an integer value is entered in the product price.")
product_quantity = int(input("Enter the products for buying: "))
product_price = int(input("Enter the price of the product: "))
amount_pay = product_quantity * product_price
print(f"the total amount to pay for client is: {amount_pay}")