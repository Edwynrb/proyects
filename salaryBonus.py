print("Calculate the salary to be paid from a worker,  entering the name, base salary and number of children;  Consider that for each child, a bonus of $ 10 is given.")
# create one constans and two variables 
BONUS_SALLARY = 10
name_operator = input("Enter name of operator: ")
base_salary = int (input("Enter salary of operator: $"))
number_sons = int(input("Enter numbers of sons: "))
# Operation for resolve operation
total_salary =  base_salary + (number_sons * BONUS_SALLARY)
print(f"The total salary of the operator {name_operator} is ${total_salary:.2f} and have {number_sons} sons..")
