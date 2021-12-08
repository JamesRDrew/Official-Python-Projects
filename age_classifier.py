#This program is used to classify a person based on age

#Get age from user

age = int(input('Please enter your age: '))

#Display classification based on age

if age <= 1:
    print('You are an infant. ')
elif age > 1 and age <= 12:
    print('You are a child. ')
elif age >= 13 and age <= 19:
    print('You are a teenager. ')
else:
    print('You are an adult. ')




