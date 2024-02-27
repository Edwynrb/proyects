# Make a program that shows the area and perimeter of a trapezio.

# Get user input
base_trap_one  = int(input("Enter the firts base of trapezio: "))
base_trap_two  = int(input("Enter the second base of trapezio: "))
height_trap    = int(input("Enter the height of the trapezio: "))
side_one       = int(input("Enter firts side :"))
side_two       = int(input("Enter the second side :"))
# Algorithms for resolve trapezio
area_trap      = 1/2 * (base_trap_one+ base_trap_two)*height_trap
perimeter_trap = base_trap_one + base_trap_two + side_one + side_two
# Display results  
print(f"The area of the trapezio is: {area_trap} and the perimeter is: {perimeter_trap}")
