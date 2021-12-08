# This program is used to calculate profit for a company based off 23
# percent of their projected total sales.

projected_sales = float(input('Please enter projected amount of total sales: $ '))

#Calculate annual profit based on 23 percent of total sales
PROFIT = float('0.23')

projected_profit = projected_sales * PROFIT

#Display information for user
print(f' Your projected annual profit is: ${projected_profit: ,.2f} ')

      

