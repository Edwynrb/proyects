# Make a program that shows the area and perimeter of a parallelogram. 

# Get user input
base_parallelogram    = int(input("Enter base of parallelogram: "))
height_parallelogram  = int(input("Enter height of parallelogram: "))
side_length           = int(input("Enter the side length of the parallelogram: "))
# Algorithms for resolve parallelogram 
area_parallelogram      = base_parallelogram * height_parallelogram
perimeter_parallelogram = 2 * (base_parallelogram + side_length)
# Display results
print(f"The area of a parallelogram is: {area_parallelogram} and the perimeter is: {perimeter_parallelogram}")