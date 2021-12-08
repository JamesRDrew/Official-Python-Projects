# This program calculates the distance traveled for each hour of a trip

# Get the number of hours traveled and the speed

time = int(input('How many hours did you travel? '))
speed = int(input('How fast were you going (MPH)? '))

print('Hour', ' ', 'Distance')


#Create a loop that calculates distance traveled each hour.

for x in range(time):
    
    distance = speed * (x + 1)

    print(x + 1 , '    ', distance )
    
    
   
    
    

            
            

