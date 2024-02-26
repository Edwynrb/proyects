# Enter the current date and show the total number of days after the beginning of this year,
# considering that every month are 30 days.

# Get user input
current_days   = int(input("Enter the current days: "))
current_months = int(input("Enter the currents months: "))
current_years  = int(input("Enter the currents years: "))
MONTHS_DAYS   = 30
# Algorithms for resolve days in this year
remmaining_days_year = current_days + (current_months *  MONTHS_DAYS)
# Display result 
print(f"{current_years} have elapsep this days {remmaining_days_year} days....")
 