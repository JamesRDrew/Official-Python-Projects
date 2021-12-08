# This Program calculates feet to inches using functions

# Create the needed functions

def main():
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        inches = feet_to_inches()
        display(inches)
        keep_going = another_round()
    print('Thank You.')

# Get the number of feet from user and convert it to inches.

def feet_to_inches():
    feet = int(input('Please enter the number of feet: '))
    while feet == 0:
        feet = int(input('ERROR Please enter a valid # other than 0: '))
    inches = feet * 12
    return inches


# Display information for user

def display(inches):
    print(f'The total number of inches is {inches}. ')

# Sentinel function

def another_round():
    print('Would you like to convert another value? ')
    keep_going = input('Enter y or Y to continue: ')
    return keep_going

# Call the main function

main()

    
               

    
