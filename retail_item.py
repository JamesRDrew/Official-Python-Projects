# This program is designed to store and display data about an item
# in a retail store

class RetailItem:
    # Initialize class and attributes 
    def __init__(self, item_descrip, inv_units, price):
        self.__item_descrip = item_descrip
        self.__inv_units = inv_units
        self.__price = price

    # Getters and setters for attributes
    def set_item_descrip(self, item_descrip):
        self.__item.descrip = item_descrip
    def get_item_descrip(self):
        return self.__item_descrip

    def set_inv_units(self, inv_units):
        self.__inv_units = inv_units
    def get_inv_units(self):
        return self.__inv_units

    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price

    

def main():
    # Create the 3 intstances of the object

    item1 = RetailItem('Jacket', 12,  59.95)
    item2 = RetailItem('Designer Jeans', 40, 34.95)
    item3 = RetailItem('Shirt', 20, 24.95)

    # Get and display the information from each object

    # Item 1 
    descrip_1 = item1.get_item_descrip()
    inv_1 = item1.get_inv_units()
    price_1 = item1.get_price()

    # Item 2 
    descrip_2 = item2.get_item_descrip()
    inv_2 = item2.get_inv_units()
    price_2 = item2.get_price()

    # Item 3
    descrip_3 = item3.get_item_descrip()
    inv_3 = item3.get_inv_units()
    price_3 = item3.get_price()

    # Display

    print(f'Item #1: {descrip_1}')
    print(f'Units in Inventory: {inv_1}')
    print(f'Price: ${price_1}')

    print('')
    
    print(f'Item #2: {descrip_2}')
    print(f'Units in Inventory: {inv_2}')
    print(f'Price: ${price_2}')

    print('')
               
    print(f'Item #3: {descrip_3}')
    print(f'Units in Inventory: {inv_3}')
    print(f'Price: ${price_3}')
          
if __name__ == '__main__':
    main()
