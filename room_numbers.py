# This program contains 3 dictionaryies with the same keys
# and returns 3 vaulues in a search function

def main():

    #Create the needed dictionaries
    room_number = {'CS101' :  '3004',  'CS102' : '4501',  'CS103' : '6755',
                               'NT110' : '1244', 'CM241' : '1411'}
    instructor = {'CS101' : 'Haynes', 'CS102' : 'Alvarado', 'CS103' : 'Rich',
                        'NT110' : 'Burke', 'CM241' : 'Lee'}
    meeting_time = {'CS101' : '8:00 a.m.', 'CS102' : '9:00 a.m.',
                              'CS103' : '10:00 a.m.', 'NT110' : '11:00 a.m.',
                              'CM241' : '1:00 p.m.'}

    # Get the course number as input
    #query = input('Please enter the course number you wish to search: ')
    #query = query.upper()
    kg = 'y'

    while kg == 'y':

        # Get the course number as input
        query = input('Please enter the course number you wish to search: ')
        query = query.upper()
        
        if query in room_number:
        
            # Pull needed information from the three dictionaries 
            number = room_number[query]
            taught_by = instructor[query]
            time = meeting_time[query]
            print(f'For course {query} you will meet in room {number} '
                  f'with Professor {taught_by} at {time}')
            kg = 'n'
        
        else:
            print('Invalid course number. Please try again')
            query = input('Please enter the course number you wish to search: ')
            query = query.upper()
            kg = 'y'

        kg = input('Would you like to search another class?'
                   ' Y for yes, press any other key for no: ')

    print('Thank you.')
       


    
    
    
    










if __name__ == '__main__':
    main()
