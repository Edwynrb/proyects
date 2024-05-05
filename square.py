# Statement of the problem
"""
Make a program that shows the area and perimeter of a square.
 """
"""
# Create variables and input user
side_length      = int(input("Enter side of the square: "))
perimeter_square = side_length * 4
square_area      = side_length * side_length

# Output for screen 
print(f"The area of the square is : {square_area} and the perimeter of the square area is: {perimeter_square} ")

"""
class Square:
    def __init__(self):
        self.side = int(input("Enter the side of the square area: "))
        
    def calculate_square(self):
        return self.side **2
    def calculate_perimeter(self):
        return self.side * 4  
    
square = Square()
total_square= square.calculate_square()
total_perimeter = square.calculate_perimeter()
print(f"The square area is:{total_square} and the Perimeter is:{total_perimeter}")
        