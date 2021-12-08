# This program uses classes and subclasses to store information about employees

# Create class Employee and sublass Production worker
class Employee():
    def __init__(self, employee_name, number):
        self.__employee_name = employee_name
        self.__number = number

    def set_name(self, employee_name):
        self.__employee_name = employee_name
    def get_name(self):
        return self.__employee_name

    def set_number(self, number):
        self.__number = number
    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, employee_name, number, shift_num, pay_rate):
        Employee.__init__(self, employee_name, number)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

    def set_shit_num(self, shift_num):
        self.__shift_num = shift_num
    def get_shift_num(self):
        return self.__shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    def get_pay_rate(self):
        return self.__pay_rate


def main():

    # Get user to input employee information
    name = input('Please enter Employee name: ')
    number = input(f"Please enter {name}'s number: ")
    sub = input(f'Is {name} a production worker? Y or N: ')
    sub.lower()
    if sub == 'y':
        err = 'y'
        while err == 'y':
            try:

                shift_num = int(input(f'Please enter which shift {name} '
                                      f'works: '))
                pay_rate = int(input(f"Please enter {name}'s hourly pay: "))

                production_worker1 = ProductionWorker(name, number, shift_num,
                                              pay_rate)
                print(f'Employee Name:{production_worker1.get_name()}')
                print(f'Employee Number:{production_worker1.get_number()}')
                print(f'Shift Number:{production_worker1.get_shift_num()}')
                print(f'Pay Rate:${production_worker1.get_pay_rate()} ')
                err = 'n'

            except ValueError:
                print('Shift Number and Pay Rate must be valid Integers.')
                err = 'y'
    else:
        employee1 = Employee(name, number)
        print(f'Employee Name:{employee1.get_name()}')
        print(f'Employee Number:{employee1.get_number()}')


if __name__ == '__main__':
    main()




