"""
Make a program to convert a length entered in to in to feet. 
"""

# Get user input
quantity_meter = int(input("Enter quantity of meters: "))
METER_FEED     = 3.28084 
# Algoritmhs of calculate length to feed 
meter_to_feed  = quantity_meter * METER_FEED
meter_to_feed_round = round(meter_to_feed, 3)
# Display results
print(f"The convertions of meters to feet is: {meter_to_feed_round}")