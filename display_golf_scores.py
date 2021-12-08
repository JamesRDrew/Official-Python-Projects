# This program reads and displays the golf_scores.txt file.

#Define main

def main():
    
        records = open('golf_scores.txt', 'r')

        # Read the file contents
        contents = records.read()

        # Close file
        records.close()
        
        print('Golfer names and scores: ')
        print(contents)

if __name__ == '__main__':
    main()
        
        
