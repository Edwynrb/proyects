""" 
# Find the surface area of a square knowing the value of one side
Input Validation Loop: Added a while loop to continuously prompt the user until valid input is provided.

# Empty Input Check: Added a check to ensure that the input is not empty or contains only whitespace characters. 
If the input is empty, an error message is printed, and the loop continues.

# ValueError Handling: Wrapped the conversion of user input to a float inside a try-except
block to handle the case where the input cannot be converted to a float (i.e., if it's not a valid numerical value).

# Positive Number Check: Added a check to ensure that the input value is greater than zero. 
If the value is less than or equal to zero, an error message is printed, and the loop continues.

# We prompt the user to enter the length of one side of the square until they type "done" to finish.
The valid side lengths are stored in a list side_lengths.
We calculate the surface area for each side length and store it in a dictionary surface_area_dict, where the side length is the key and the surface area is the value.
Finally, we print the surface area for each side length stored in the dictionary.

# Convert in function

# Convert in oop 

# Convert in crud with mysql and sqlite

# Convert to tinker
"""

"""
# Get user input
side_length = int(input("Enter the side length of the surface area: "))

# Algoritmhs for result surface area
surface_area = side_length * side_length

# Display results
print(f"The surface area of the square is: {surface_area}")

"""
"""
# this is the function for calculate the side length of the surface area
def surface_area(a):
    return a*a
# ask the user for a value 
side_length = int(input("Enter the side length of the surface area: "))
# invoke function to calculate surface area of the square 
print(f"the surface of the square is: {surface_area(side_length)}")
"""
""" 
# convert app in oriented programaming languajes
class Surface_area:
    def __init__(self, side_length):
        # initialize constructor method to initialize the surface object with side length 
        self.side_length = side_length
        
    def calculate_surface_area(self, side_length):
        return side_length*side_length 
# Example usage:
if __name__ == "__main__":
    # Example value
    side_length = int(input("Enter the side length of the square: "))
    # Creating an instance of the Surface class
    surface_area = Surface_area(side_length)
    # Calculating the surface area of the square
    surface_area_square = surface_area.calculate_surface_area(side_length)
    # Printing the monthly salary
    print(f"the surface area of the square is: {surface_area_square}")
"""
import tkinter as tk

class SurfaceAreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Surface Area Calculator")

        self.label = tk.Label(root, text="Enter the side length of the square:")
        self.label.pack()

        self.side_length_entry = tk.Entry(root)
        self.side_length_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate Surface Area", command=self.calculate_surface_area)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate_surface_area(self):
        try:
            side_length = float(self.side_length_entry.get())
            surface_area = side_length * side_length
            self.result_label.config(text=f"The surface area of the square is: {surface_area}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SurfaceAreaCalculator(root)
    root.mainloop()


    
    