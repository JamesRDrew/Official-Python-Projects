# This program is designed to write a class and subclass about a person

class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name
    def  get_name(self):
        return self.__name

    def set_address(self, address):
        self.address = address
    def get_address(self):
        return self.__address

    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone

class Customer(Person):
    def __init__(self, name, address, phone, cust_num, mail_list):
        Person.__init__(self, name, address, phone)
        self.__cust_num = cust_num
        self.__mail_list = mail_list


    def set_cust_num(self, cust_num):
        self.__cust_num = cust_num
    def get_cust_num(self):
        return self.__cust_num

    def set_mail_list(self, mail_list):
        self.__mail_list = mail_list
    def get_mail_list(self):
        return self.__mail_list


def main():
    start = input('Would you like to sign up a customer? Y or N: ')
    start.lower()
    if start == 'y':
        name = input('Enter name: ')
        address = input('Enter address: ')
        phone = input('Enter Phone Number: ')
        cust_num = input('Enter customer number: ')
        start_mail = input('Would this customer like to recieve mail? y or '
                           'n: ')
        start_mail.lower()
        if start_mail == 'y':
            mail_list = True
        else: mail_list = False

        # Create an object of this customer
        customer1 = Customer(name, address, phone, cust_num, mail_list)

        print()
        print('Customer information:')
        print(f'Name: {customer1.get_name()}')
        print(f'Address: {customer1.get_address()}')
        print(f'Phone: {customer1.get_phone()}')
        print(f'Customer Number: {customer1.get_cust_num()}')
        print(f'Mailing List: {customer1.get_mail_list()}')

if __name__ == '__main__':
    main()