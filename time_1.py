print("Make an algorithm where an amount of seconds is entered and show the hours, minutes and seconds in tha amount. Make an algorithm to show the hours, minutes and seconds in a total number of seconds entered by keyboard.")

# Get user input:
second_time = int(input("Enter number of seconds: "))

# Make variables or constant 
hour_seconds = second_time // 3600
minutes_seconds = second_time // 60
seconds = second_time % 60


# Display the result:
print(f"{second_time} Seconds is equal to {hour_seconds} hours, {minutes_seconds} Minutes in {seconds} seconds")

""" 
def convert_seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

def main():
    total_seconds = int(input("Enter the total number of seconds: "))
    hours, minutes, seconds = convert_seconds_to_hms(total_seconds)
    print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

if __name__ == "__main__":
    main()
"""