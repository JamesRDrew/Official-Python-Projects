# This program lists monthly costs of automobile maintinance entered by the
# user and adds them up for a total annual cost.

# Create the main function

def main():
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        loan = get_loan()
        insurance = get_insurance()
        gas = get_gas()
        oil = get_oil()
        tires = get_tires()
        maintenance = get_maintenance()
        annual_cost = calc_annual_total(loan, insurance, gas, oil, tires,
                                        maintenance)
        display_cost (loan, insurance, gas, oil, tires, maintenance,
                      annual_cost)
        keep_going = another_round()
    print('Thank You.')
    
    
# Create a function for each needed piece of information from the user

def get_loan():
    loan = float(input('Please enter the monthly loan payment for' 
                       ' your vehicle: $'))
    return loan

def get_insurance():
    insurance = float(input('Please enter the monthly insurance payment for '
                       'your vehicle: $'))
    return insurance

def get_gas():
    gas = float(input('How much do you spend on gas monthly?: $'))
    return gas

def get_oil():
    oil = float(input('How much do you spend on oil monthly?: $'))
    return oil

def get_tires():
    tires = float(input('How much do you save for tires monthly?: $'))
    return tires

def get_maintenance():
    maintenance = float(input('How much do you spend on'
                              ' maintenance monthly?: $'))
    return maintenance

#Create a function for adding together info and the annual total

def calc_annual_total(x1, x2, x3, x4, x5, x6):
    annual_cost = (x1 + x2 + x3 + x4 + x5 +x6) * 12
    return annual_cost

def display_cost(loan, insurance, gas, oil, tires, maintenance, annual_cost):
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')
    print('Your monthly costs are as follows: ')
    print(f'Loan payment: ${loan: .2f} ')
    print(f'Insurance payment ${insurance: .2f} ')
    print(f'Gas expenses: ${gas: .2f} ')
    print(f'Oil expenses: ${oil: .2f} ')
    print(f'Money saved for tires: ${tires: .2f} ')
    print(f'Monthly maintenance costs: ${maintenance: .2f}  ')
    print(f'This gives you an annual cost of: ${annual_cost: .2f} ')

def another_round():
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')
    print('Would you like to input values for another vehicle??')
    keep_going = input('Enter y to input another vehicle: ')
    return keep_going
    


main()
    



   
