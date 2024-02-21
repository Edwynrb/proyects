print("A bakery sells loaves of bread for €3.49 each.  Bread that is not the same day has a 60% discount.Writea program that starts by reading the number of bars    sold that are not of the day. Then the program must    show the usual price of a loaf of bread, the discount  given for not being fresh, and the total final cost.") 
 
# declare const variables
LOAVES_BREAD_PRICE = 3.49
LOAVES_BREAD_DISCOUNT = (60/100)
# calculate discount 
discount_amount = LOAVES_BREAD_PRICE * LOAVES_BREAD_DISCOUNT
# calculated discount amount 
discount_price = LOAVES_BREAD_PRICE - discount_amount

# prompt user for input 
LOAVES_BREAD_OLD = int(input("Enter quantity of bread loaves old: "))

# calculated total cost 
total_cost = LOAVES_BREAD_OLD * discount_price

# print results 
print("The usual price of loaves bread is :${:.2f}".format(LOAVES_BREAD_PRICE))
print("Discount given for not being fresh :${:.2f}".format(discount_amount))
print("The total price is :${:.2f}".format(total_cost))
