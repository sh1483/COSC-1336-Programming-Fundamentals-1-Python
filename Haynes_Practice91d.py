# Name: Steven Haynes
# Chapter 9-1d Practice Project Status: Complete

# A program that creates a dictionary, provides a menu of choices to the user,
# and can display the entire dictionary. There will be 4 different modules,
# with the main program importing all the modules.
# Module 4, change and delete module.

# Global constants again.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
QUIT = 6


# Change function.
def change(cats):
    name = input('Enter a cat name: ')

    # Check and change.
    if name in cats:
        type = input('Enter a new type: ')
        cats[name] = type
    else:
        print('That name is not found.')


# Delete function.
def delete(cats):
    name = input('Enter a cat name: ')

    # Check and delete.
    if name in cats:
        del cats[name]
    else:
        print('That name is not found.')
