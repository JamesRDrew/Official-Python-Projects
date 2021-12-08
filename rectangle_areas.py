#This program takes the area of two rectangles and displays the larger area

#Get the dimensions of the first rectangle

width1 = float(input('Please enter the width of the first rectangle: '))
length1 = float(input('Please enter the length of the first rectangle '))

#Get the demensions of the second rectangle

width2 = float(input('Please enter the width of the second rectangle: '))
length2 = float(input('Please enter the length of the second rectangle: '))

#Calculate the area of both rectangles ]

area1 = width1 * length1
area2 = width2 * length2

#Display the larger of the two areas or if both are equal

if area1 > area2:
    print(f'The first rectangle has an area of{area1: .2f} ' 
           'so it has the larger area. ')
elif area2 > area1:
    print(f'The second rectangle has an area of{area2: .2f} '
           'so it has the larger area. ')
else:
    print('Both rectangles have the same area.')
