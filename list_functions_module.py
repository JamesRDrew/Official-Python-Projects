# This program contains useful functions in the analysis of lists.


# Create a function to get a specific number of items and write it to a list 
def get_list():

    #create list to write numbers to
    list1 = []
    print('Please enter a whole number: ')
    #Loop to get 20 numbers
    for x in range(0, 20):
        
        num = int(input(''))
        list1.append(num)

    return list1



# Create a function for the sum of the elements of a given list. 
def list_total(y):

    # Accumulator for the sum
    total = 0 
    # Use a loop to add the elements of a list
    for x in y:
        total += x

    return total 



# Create a function that finds the average of the
# elements of a list of integers
def list_average(y):

    # Accumulator for number of elements and sum of elem
    elem = 0
    total = 0
    # Use a loop to add the elems of a list and number of elems
    for x in y:
        total += x
        elem += 1

    # Average the list 
    average = total / elem

    return average




# Create a function that determines the min and max elements of a list
def list_minmax(y):
    low = min(y)
    high = max(y)

    return low, high




# Create a function that displays the information for the user
def display_info(low, high, total, average):
    print('The lowest number you entered was:', low)
    print('The highest number you entered was:', high)
    print('The sum of the numbers you entered is:', total)
    print('The average of the numbers you entered is:', average)



 
