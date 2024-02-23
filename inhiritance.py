# The statement of exercises. 
print("Make an algorithm that shows how much money he has to each one of the brothers of an inheritance that his father left them, distributing his inheritance as follows: to the older brother 50%, to the second brother 35% and the remaining brother.")

# make variables or constans
OLD_BROTHERS      = 50
SECOND_BROTHER    = 35
REMAINING_BROTHER = 15

# emter the money inheritance for the fathers. 
inheritance_broters = int(input("Enter the inheritance for brothers: $"))

# process for each childs or brothers

old_brothers      = inheritance_broters * (OLD_BROTHERS/100)  
second_brothers   = inheritance_broters * (SECOND_BROTHER/100)
remaining_broters = inheritance_broters * (REMAINING_BROTHER/100)


# result of inheritance for each childs
print("The old brothers have ${:.2f} of money".format(old_brothers))
print("The second brothers have ${:.2f} of money".format(second_brothers))
print("The remaining brothers have ${:.2f} of money".format(remaining_broters))

