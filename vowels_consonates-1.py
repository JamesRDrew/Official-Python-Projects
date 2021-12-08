# This program is designed to get a string
# from a user and count vowels and consonants

def main():

    # Get the string from user
    letters = input('Please enter the letters you want: ')
    vowels_total = vowels(letters)
    consonants_total = consonants(letters)

    
    print(f'There are {vowels_total} vowel(s) and'
          f' {consonants_total} consonant(s).')
            
        
def vowels(letters):

    # Accumulator for vowels 
    vowels = 0
    

    # Define Vowels 
    vowels_lit = 'aieou'
    
    # Loop to compare input with vowels 
    for x in letters:
        for y in vowels_lit:
            if x == y:
                vowels +=1
        

        

    return vowels

def consonants(letters):

    # Accumulator for consonants
    consonants = 0

    # Define Consonants
    cons_lit = 'bcdfghjklmnpqrstvwxyz'

    # Loop to compare input with consonants
    for x in letters:
        for y in cons_lit:
            if x == y:
                consonants +=1

    return consonants
    

if __name__ == '__main__':
    main()
