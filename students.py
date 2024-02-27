# Enter the number of approved and disapproved students ofa course, then show the percentage of approved students 
# and the percentage of disapproved students.

# Get user input
students_approved    = int(input("Enter approved students: "))
students_disapproved = int(input("Enter disapproved students: "))

# Algorithms for resolve students approved and disapprove

total_students               = students_approved + students_disapproved

percentage_approved          = (students_approved / total_students) * 100

percentage_disapproved       = (students_disapproved / total_students) * 100

percentage_approved_round    = round(percentage_approved,2)

percentage_disapproved_round = round(percentage_disapproved,2)
# Display results 
print(f"The total students are: {total_students}")
print(f"The total students approved are: {students_approved}")
print(f"The total students disapproved are: {students_disapproved}")
print(f"The percentage of students approved are: {percentage_approved_round}%")
print(f"The percentage of students disapproved are: {percentage_disapproved_round}%")

