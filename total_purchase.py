# This program gets prices from a customer and calculates sales tax

SALES_TAX = .07
def main():
    total = 0
    err = 'y'
    while err == 'y':
        try:
            x = int(input('How many items are you purchasing? '))
            count = 0
            for y in range(x):
                count += 1
                price = int(input(f'What is the price of item # {count} '))
                total += price
            err = 'n'
        except ValueError:
            print('Number of items and price must be valid integers.')
            err = 'y'
    tax = total * SALES_TAX
    total = total - tax
    print(f'Your total is ${total: .2f}')

if __name__ == '__main__':
    main()

