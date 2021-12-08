# This program is designed to get a users name and display the initials

def main():

    # Get users name
    first_name = input('Please enter your first name: ')
    keep_going = input('Do you have a middle name? Y or N: ')
    if keep_going == 'y' or keep_going == 'Y':
        middle_name = input('Please enter your middle name: ')
    else:
        middle_name = ''
    last_name = input('Please enter your last name: ')
    if middle_name == '':
        print(f'Your inititals are {first_name[0]}.{last_name[0]}')
    else:
        print('Your inititals are '
              f'{first_name[0]}.{middle_name[0]}.{last_name[0]}')
    
    


if __name__ == '__main__':
    main()
