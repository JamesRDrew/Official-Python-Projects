# This program gets projected sales and outputs total sales prediction

PROFIT = 0.23
def main():
    sales = int(input('Please enter predicted sales: '))
    total = sales * PROFIT

    print(f'Your projected sales are ${total: .2f}')

if __name__ == '__main__':
    main()