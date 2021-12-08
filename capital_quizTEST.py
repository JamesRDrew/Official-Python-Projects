# This program uses a dictionary of states and capitals and quizes the user

import random


def main():
    k_g = 'y'

    while k_g == 'y' or k_g == 'Y':
        # Get dictionary
        capitals = state_cap_dict()
        # Get number of states to be quizzed on by user
        number = int(input('How many states would you like '
                           'to be quizzed on? '))
        # Initialize accumulators for right and wrong answers
        correct = 0
        incorrect = 0

        # Create a loop to quiz user and record correct or incorrect

        for x in range(number):
            # Get a random entry from dictionary
            state, capital = capitals.popitem()

            # Quiz the user
            response = input(f'What is the Capital of {state}? ')

            # Record if correct or incorrect
            if response.lower() == capital.lower():
                correct += 1
                print('Correct!')

            else:
                incorrect += 1
                print('Incorrect')

        print(f'You got {correct} answers correct and {incorrect}'
              ' answers incorrect.')

        k_g = input('Would you like to play again? Y for yes'
                    ' or any other key for No: ')

    print('Thank You')


# A function that creates the dictionary of states and capitals
def state_cap_dict():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
                "Arizona": 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento',
                'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover',
                'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
                'Idaho': 'Boise',
                'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
                'Iowa': 'Des Moines',
                'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
                'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta', 'Maryland': 'Annapolis',
                'Massachusetts': 'Boston',
                'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
                'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City', 'Montana': 'Helena',
                'Nebraska': 'Lincoln',
                'Nevada': 'Carson City', 'New Hampshire': 'Concord',
                'New Jersey': 'Trenton',
                'New Mexico': 'Santa Fe', 'New York': 'Albany',
                'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
                'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence',
                'South Carolina': 'Columbia',
                'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
                'Texas': 'Austin', 'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier',
                'Virginia': 'Richmond', 'Washington': 'Olympia',
                'West Virginia': 'Charleston',
                'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    return capitals


# Call main function
if __name__ == '__main__':
    main()
