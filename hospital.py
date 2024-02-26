# Make a program where the annual budget of a hospital is distributed in the following areas:  
# 40 gynecology, 30% traumatology and 30% pediatrics, of a total amount of money assigned.

# Get user input
annual_budget = int(input("Enter the annual budget for hospital: $"))
# Algorithms for result hospital
GYNECOLOGY_BUDGET   = annual_budget *  (40/100)
TRAUMATOLOGY_BUDGET = annual_budget *  (30/100)
PEDIATRICS_BUDGET   = annual_budget * (30/100)
# Display results
print("The annual budget for area of ginecology is: ${:.2f} of money".format(GYNECOLOGY_BUDGET))
print("The annual budget for area of traumatology is: ${:.2f} of money".format(TRAUMATOLOGY_BUDGET))
print("The annual budget for area of pediatrics is: ${:.2f} of money".format(PEDIATRICS_BUDGET))