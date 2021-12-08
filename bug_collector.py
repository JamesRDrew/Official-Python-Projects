# This program is used to add the amount of bugs collected over a 7 day period

# Define accumulator

total = 0

# Create loop to ask for the bugs counted over 7 days

for days in range (1, 8):
    bugs = int(input(f'Please enter the bugs collected in day {days}: '))
    # Add the bugs collected that day to the total 
    total = bugs + total

# Display the total

print(f'You have collected {total} bugs this week. ')







    
