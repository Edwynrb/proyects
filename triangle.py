print("Make a program that shows the area and perimeter of a triangle.")
# Create variables and input user
side_length_one   = int(input("Enter the first side of a triangle: "))
side_length_two   = int(input("Enter the second side of a triangle: "))
side_length_three = int(input("Enter the third side of a triangle: "))

# Process to resolve exercises
perimeter_triangle = side_length_one + side_length_two + side_length_three
semi_perimeter     = (perimeter_triangle/2)
area_triangle      = (semi_perimeter*(semi_perimeter-side_length_one)*(semi_perimeter-side_length_two)*(semi_perimeter-side_length_three))**0.5
area_triangle_round = round(area_triangle,2)
# Result of the perimeter and area of a triangle
print(f"The sides of the triangle are: {side_length_one} , the second {side_length_two} and the third {side_length_three}")
print(f"The perimeter of a triangle is: {perimeter_triangle}")
print(f"The semi perimeter is: {semi_perimeter}")
print(f"The area of a triangle is: {area_triangle_round}")