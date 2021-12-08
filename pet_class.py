# This program is designed to use a
# pet class to store information about a pet from a user.

class Pet:

    # Create a method to initialize attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Setters and getters for each attribute
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def get_animal_type(self):
        return self.__animal_type

    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age

    
# Use the main program to creat an instance
# of Pet and get/record the data from user. 
def main():

    print('Please enter information about your pet!')

    name = input('Name: ')
    animal_type = input(f'What type of animal is {name}? ')
    age = input(f'How old is {name}? ')

    my_pet = Pet(name, animal_type, age)

    # Retrieve data from the object and display for user
    
    name = my_pet.get_name()
    animal_type = my_pet.get_animal_type()
    age = my_pet.get_age()
    print(f"Your {animal_type}'s name is {name} and they're {age} years old. ")
    
          


if __name__ == '__main__':
    main()
