print("make a program that calculates the total area of a cylinder and its volume, entering radio (R) and     height (h) as income data.")
PI= 3.14
radio_cylinder = int(input("Enter radio of cylinder: "))
height_cylinder =int(input("Enter height of cylinder: "))

# formula for surface area
surface_area = 2 * PI * (radio_cylinder)**2 + 2 * PI * radio_cylinder * height_cylinder

# formula of volume 
volume_cylinder = PI * (radio_cylinder)**2 * height_cylinder

print(f"The surface area of cylinder is: {surface_area}")
print(f"The volume of cylinder is: {volume_cylinder}")
