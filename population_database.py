# This program works with a created database to organize information

import sqlite3

# Main function

def main():
    # Menu choice
    choice = 0

    # Connect to database
    conn = sqlite3.connect('cities.db')

    # Get a cursor
    cur = conn.cursor()

    # Get the users menu choice
    while choice != 8:
        choice = get_menu_choice()
        execute_choice(choice, cur)

    # Close the connection
    conn.close()

def display_menu():
    print('                          MENU')
    print('--------------------------------------------------------')
    print('1 - Display cities sorted by population, ascending order')
    print('2 - Display cities sorted by population, descending order')
    print('3 - Display cities sorted by name')
    print('4 - Display total population of all the cities')
    print('5 - Display average population of all the cities')
    print('6 - Display city with the highest population')
    print('7 - Display city with the lowest population')
    print('8 - EXIT')

def get_menu_choice():
    display_menu()
    choice = int(input('Enter your choice: '))
    # Validate the choice
    while choice < 1 or choice > 8:
        choice = int(input('Enter a valid choice: '))
    return choice

def execute_choice(choice, cur):
    if choice == 1:
        cities_sorted_ascending(cur)
    elif choice == 2:
        cities_sorted_descending(cur)
    elif choice == 3:
        cities_sorted_by_name(cur)
    elif choice == 4:
        total_population(cur)
    elif choice == 5:
        average_population(cur)
    elif choice == 6:
        highest_population(cur)
    elif choice == 7:
        lowest_population(cur)

def cities_sorted_ascending(cur):
    # Excecute the SELECT statement on the database
    cur.execute('''SELECT CityName, Population 
                   FROM Cities
                   ORDER BY Population''')

    # Fetch the results
    results = cur.fetchall()

    # Display the results
    print('\nCities Sorted By Population in Ascending Order')
    print('------------------------------------------------')
    display_results(results)

def cities_sorted_descending(cur):

    # Execute the SELECT statement on the databse
    cur.execute('''SELECT CityName, Population
                   FROM Cities 
                   ORDER BY Population DESC''')

    # Fetch Results
    results = cur.fetchall()

    # Display Results
    print('\nCities Sorted By Population in Descending Order')
    print('-------------------------------------------------')
    display_results(results)

def cities_sorted_by_name(cur):
    # Execute the SELECT statement on the databse
    cur.execute('''SELECT CityName, Population
                      FROM Cities 
                      ORDER BY CityName''')

    # Fetch Results
    results = cur.fetchall()

    # Display Results
    print('\nCities Sorted By Name')
    print('-------------------------------------------------')
    display_results(results)

# Display the Total Population
def total_population(cur):
    # Execute the SELECT statement on the databse
    cur.execute('SELECT SUM(Population) FROM Cities')

    # Fetch Results
    results = cur.fetchone()

    # Display Results
    print(f'\nTotal Population: {results[0]:,.0f}\n')

# Display the Average Population
def average_population(cur):
    # Execute the SELECT statement on the databse
    cur.execute('SELECT AVG(Population) FROM Cities')

    # Fetch Results
    results = cur.fetchone()

    # Display Results
    print(f'\nAverage Population: {results[0]:,.0f}\n')

# Display the Highest Population
def highest_population(cur):
    cur.execute('SELECT MAX(Population) FROM Cities')

    # Fetch Results
    max_results = cur.fetchone()

    # Get entire row that contains that population
    cur.execute('''SELECT CityName, Population FROM Cities 
                   WHERE Population = ?''', (max_results[0],))

    # Fetch results
    results = cur.fetchone()

    # Display the results
    print(f'\n{results[0]} has the Highest Population: {results[1]:,.0f}\n')

#Display the Lowest Population
def lowest_population(cur):
    cur.execute('SELECT MIN(Population) FROM Cities')

    # Fetch Results
    min_results = cur.fetchone()

    # Get entire row that contains that population
    cur.execute('''SELECT CityName, Population FROM Cities 
                   WHERE Population = ?''', (min_results[0],))

    # Fetch results
    results = cur.fetchone()

    # Display the results
    print(f'\n{results[0]} has the Lowest Population: {results[1]:,.0f}\n')

#Display the Results
def display_results(results):
    print(f'{"City":20}{"Population"}')
    for row in results:
        print(f'{row[0]:20}{row[1]:,.0f}')
        print()

# Execute Main
if __name__ == '__main__':
    main()
