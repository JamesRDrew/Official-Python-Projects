# This program uses classes to simulate shopping

import cash_register

def initialize_obj():
    # Create the 3 intstances of the objects available for purchase
    jacket = cash_register.RetailItem('Jacket', 12, 59.95)
    jeans = cash_register.RetailItem('Designer Jeans', 40, 34.95)
    shirt = cash_register.RetailItem('Shirt', 20, 24.95)

    # Instantiate the CashRegister Object
    register = cash_register.CashRegister()

    return jacket, jeans, shirt, register

def menu():
    # Create a menu for the user
    print('1: Add an item to your shopping cart.')
    print('2: Clear shopping cart. ')
    print('3: Check out.')
    print('4: Exit.')

    selection = int(input('Please enter an option number to continue: '))
    print('')
    return selection

def buy_items(jacket, jeans, shirt, register):
    # Loop to stay in section 1
    k_g = 'y'
    while k_g == 'y':
        # Display items for sale
        print(f'1: {jacket.get_item_descrip()} - ${jacket.get_price()}')
        print(f'2: {jeans.get_item_descrip()} - ${jeans.get_price()}')
        print(f'3: {shirt.get_item_descrip()} - ${shirt.get_price()}')
        choice = int(input('Please enter the number for your item: '))

        # Put selected items into shopping cart list
        if choice == 1:
            register.purchase_item(jacket)
            print(f'{jacket.get_item_descrip()} has been added to '
                  f'the cart.')
            print('')
            print('')

        if choice == 2:
            register.purchase_item(jeans)
            print(f'{jeans.get_item_descrip()} has been added to the '
                  f'cart.')
            print('')
            print('')

        if choice == 3:
            register.purchase_item(shirt)
            print(f'{shirt.get_item_descrip()} has been added to the '
                  f'cart.')
            print('')
            print('')

        k_g = input('Would you like to add another item? press y to '
                    'add '
                    'or any other key top return.')
        print('')
        k_g = k_g.lower()
    else:
        return k_g, register



def main():
    # Call initialize function to create needed objects
    jacket, jeans, shirt, register = initialize_obj()
    start = 'y'
    while start != 'n':
        selection = menu()
        # Create options for selection 1
        if selection == 1:
            k_g, register = buy_items(jacket, jeans, shirt, register)
            if k_g != 'y':
                start = 'y'

        # Create options for selection 2
        if selection == 2:
            register.clear()
            print('')

        # Create options for selection 3
        if selection == 3:
            register.show_items()
            total = register.get_total()
            print(f'Total: {total: .2f}')
            checkout = input('Would you like to check out? Y or N: ')
            checkout = checkout.lower()
            if checkout == 'y':
                print('Thank You. ')
                start = 'n'


        if selection == 4:

            print('Thank You. ')
            start = 'n'



if __name__ == '__main__':
    main()

