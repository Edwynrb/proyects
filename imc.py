print(" Write a program that asks the user for their weight (in kg) and height (in meters), calculates the body mass index and stores it in a variable, and displays on the screen the sentence where is the calculated body mass index rounded Tu índice de masa corporal es <imc>with <imc>two decimals.")

weight_person = int(input("Enter weight of the person "))
height_person = float(input("Enter height of the person "))
imc_person = weight_person * (height_person)**2
print(f"The index mass of the person is {imc_person}")

