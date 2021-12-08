# This program reads numbers from a txt file and adds
# them together to display the sum.

# Create main function

def main():

    # Open the file

    numbers = open('numbers.txt' , 'r')
    total = read_file(numbers)

    # Close the file
    numbers.close()
    
    print('The sum of the numbers in the file is', total)

    
# Create the loop that will read the numbers and add them.

def read_file(numbers):
    

    # Initialize an accumulator
    total = 0.0
    
    for line in numbers:
        #Convert the numbers to int
        numbers = int(line)

        #Add the numbers to the accumulator
        total = total + numbers

    return total


# Call the main function
if __name__ == '__main__':
    main()
        
