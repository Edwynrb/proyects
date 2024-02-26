# Enter a number of days and show the number of years,
# months and days in the value entered; 
# Consider that every month are 30 days.

# Get user input
days_time = int(input("Enter numbers of day: "))
# Algorithms for result days to years
year_day   = days_time //  365
months_day = days_time // 30
# Display the result
print(f"{days_time} days This is the conversion the day to years: {year_day} and the quantity the months are: {months_day}")