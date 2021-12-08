# This program is designed to get 20 numbers from the user write a list 
# display info about it. 

import list_functions_module

def main():
    # Get the numbers from the user and create a list
    numbers = list_functions_module.get_list()

    # Perform the needed analysis of the list and display it 
    low, high = list_functions_module.list_minmax(numbers)
    total = list_functions_module.list_total(numbers)
    average = list_functions_module.list_average(numbers)
    list_functions_module.display_info(low, high, total, average)
    
if __name__ == '__main__':
    main()
