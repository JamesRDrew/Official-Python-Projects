# This program computes ste and county sales tax of an inputed value

STATE = .05
COUNTY = .025

def main():
    con = 'y'
    while con == 'y':
        try:
            price = int(input('Please enter the price of the item: '))
            state_tax = price * STATE
            county_tax = price * COUNTY
            total_tax = state_tax + county_tax
            total = total_tax + price
            con = 'n'

        except ValueError:
            print('Price must be a valid integer. ')
            con = 'y'

    print(f'The state tax is ${state_tax: .2f}')
    print(f'The county tax is ${county_tax: .2f}')
    print(f'The total amount of tax is ${total_tax: .2f}')
    print(f'The total purchase price ${total: .2f}')

if __name__ == "__main__":
    main()


