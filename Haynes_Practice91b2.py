# Name: Steven Haynes
# Chapter 9-1b2 Practice Project Status: Complete

# A program that creates a dictionary, provides a menu of choices to the user,
# and can display the entire dictionary. There will be 4 different modules,
# with the main program importing all the modules.
# Module 2, get_menu_choice and look_up module.

# Global constants
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
SAVE = 6
RETRIEVE = 7
QUIT = 8


# Create the menu.
def get_menu_choice():

    print()
    print('Types of cats')
    print('_____________')
    print('1. Look up a cat.')
    print('2. Add a cat.')
    print('3. Change a cat.')
    print('4. Delete a cat.')
    print('5. Show all cats.')
    print('6. Save cats.')
    print('7. Get cats.')
    print('8. Quit the program.')
    print()

    choice = int(input('Enter your choice: '))

    # In case of choice error.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # Return the choice.
    return choice


# Look up function.
def look_up(cats):
    name = input('Enter a cat name: ')
    print(cats.get(name, 'Not found.'))
