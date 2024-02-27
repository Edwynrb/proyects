# Generate a program that allows to calculate the final salary of an employee,
# if it is known that the salary increases at $ 100 for each child and in $ 25 for each non-working day that the worker attended. 
# You must enter by keyboard: the base salary, the number of children and the number of non-working days that attended the worked.

# Get user input
hours_worked    = int(input("Enter the hours worked for employee: "))
value_per_hour  = int(input("Enter the value per hour: "))
num_childs      = int(input("Enter numbers of childs please: "))
non_working_day = int(input("Enter numbers of non working day of employee: "))
# Algorithms for result final salary 
final_salary = hours_worked * value_per_hour * num_childs* non_working_day

# Display result
print(f"The hours worked for employee are: ")
print(f"The value per hours is: ")
print(f"The employee have this numbers of childs: ")
print(f"The employee have this numbers of day non worked")
print("The total salary of the operator is: ${:.2f}".format(final_salary))
