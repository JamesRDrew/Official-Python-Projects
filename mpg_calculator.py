#This program is used to calculate Miles-Per-Gallon

#Get usage information from user
miles_driven = float(input('Please enter the amount of miles driven: '))
gas_used = float(input('Please enter the amount of gas used: '))

#Calculate the miles per gallon used
mpg = miles_driven / gas_used

#Display miles per gallon for user
print(f'Your miles-per-gallon usage was: {mpg: .2f}')
