# This program is used to get information from golfers and write it to a file.

# Define main

def main():

    # Create a file for the golf scores
    golf_records = open('golf_scores.txt', 'w')
    get_info(golf_records)
    print('All Player information has been written to file.')



# Create a loop that asks for golfers names and scores then write it to file.

def get_info(golf_records):
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        try:
            name = input('Please enter the player name: ')
            score = int(input(f"What was {name}'s score? "))

            # Write data to the file
            golf_records.write(f'{name}\n')
            golf_records.write(f'{score}\n')

        except ValueError:
            print('Player score must be a valid number. ')

        # Check if there's more players
        keep_going = input('Press y or Y to enter another player: ')

if __name__ == '__main__':
    main()

        

    
                
