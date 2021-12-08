# This program generates a 7 digit lottery number.

import random

def main():

    # Create a list for the numbers to be written to.
    num_list = []

    # Creat loop to generate numbers and write to list
    for x in range(0,7):
        n = random.randint(0, 61)
        num_list.append(n)

    #Display results using a loop
    print('Your lottery numbers are:')
    for x in num_list:
        print(x)


if __name__ == '__main__':
    main()
