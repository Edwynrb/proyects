# A builder knows that it needs 0.05 cubic meters of sand by square meter of revous to be made.  
# Make an algorithm that calculates the measurements of a long 
# and high wall expressed in meters and obtain the amount of sand necessary for the total revocation.

# Get user input
side_length  = int(input("Enter the side length of the wall in meters: "))
width_length = int(input("Enter the width length of the wall in meters: ")) 
# high_wall     = int(input("Enter the high wall of the builder: "))
CUBICS_METERS =  0.05
area_square   = side_length * width_length 
# Algorithms for result cubic meters of sands
amount_sand       =  area_square * CUBICS_METERS  
amount_sand_round = round(amount_sand, 2) 
# Display results
print(f"The total amount of sand needed for the revocation is: {amount_sand_round} in cubics meters")

"""
def calculate_sand_for_revocation(length, height):
    # Calculate total area of the wall
    total_area = length * height
    
    # Calculate the amount of sand needed for the total revocation
    sand_needed = total_area * 0.05
    
    return sand_needed

def main():
    # Prompt user to input the length and height of the wall
    length = float(input("Enter the length of the wall in meters: "))
    height = float(input("Enter the height of the wall in meters: "))
    
    # Calculate the amount of sand needed
    sand_needed = calculate_sand_for_revocation(length, height)
    
    # Display the result
    print("The total amount of sand needed for the revocation is:", sand_needed, "cubic meters")

if __name__ == "__main__":
    main()
"""