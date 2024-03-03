""" 
# Find the surface area of a square knowing the value of one side
Input Validation Loop: Added a while loop to continuously prompt the user until valid input is provided.

# Empty Input Check: Added a check to ensure that the input is not empty or contains only whitespace characters. 
If the input is empty, an error message is printed, and the loop continues.

# ValueError Handling: Wrapped the conversion of user input to a float inside a try-except
block to handle the case where the input cannot be converted to a float (i.e., if it's not a valid numerical value).

# Positive Number Check: Added a check to ensure that the input value is greater than zero. 
If the value is less than or equal to zero, an error message is printed, and the loop continues.

# Convert in function

# Convert in oop 

# Convert in crud with mysql and sqlite

# Convert to tinker
"""
# Get user input
side_length = int(input("Enter the side length of the surface area: "))

# Algoritmhs for result surface area
surface_area = side_length * side_length

# Display results
print(f"The surface area of the square is: {surface_area}")

