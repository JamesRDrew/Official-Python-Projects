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

# Create a class to store and process RetailItem
class CashRegister:
    # Create an internal list for use in the class
    def __init__(self,):
        self.shopping_cart = []

    # Add an object of RetailItem class when called to the list
    def purchase_item(self, Ritem):
        self.shopping_cart.append(Ritem)

    # Add all of the get_price methods from each object in the list to an
    # accumulated variable.
    def get_total(self):
        total = 0
        for x in self.shopping_cart:
            price = x.get_price()
            total += price
        return total

    # Method to display items in list
    def show_items(self):
        print('Here are the items in your shopping cart:')
        print('')
        for x in self.shopping_cart:
            item = x.get_item_descrip()
            print(item)

    def clear(self):
        self.shopping_cart.clear()
        print('The shopping cart has been cleared.')


def main():
    # Create the 3 intstances of the objects available for purchase
    jacket = RetailItem('Jacket', 12,  59.95)
    des_jean = RetailItem('Designer Jeans', 40, 34.95)
    shirt = RetailItem('Shirt', 20, 24.95)

    # Instantiate the CashRegister Object
    register = CashRegister()

    item1 = register.purchase_item(jacket)
    item2 = register.purchase_item(des_jean)
    item3 = register.purchase_item(shirt)

    total = register.get_total()
    display = register.show_items()
    print(f'Your total is ${total: .2f}')
    #print(display)

    clear = register.clear()
    print(display)





    
          
if __name__ == '__main__':
    main()
