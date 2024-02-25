# Make a program that shows the area and perimeter of a rectangle.

# Create variables and input user 
length_rectangle = int(input("Please enter length of rectangle: "))
width_rectangle  = int(input("Please enter width of rectangle: "))
# Algorithms for calculate area and perimeter of rectangle 
area_rectangle      = length_rectangle * width_rectangle 
perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
# Output for the screen 
print(f"The area of rectangle is: {area_rectangle}")
print(f"The perimeter of rectangle is: {perimeter_rectangle}")