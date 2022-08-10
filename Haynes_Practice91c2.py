# Name: Steven Haynes
# Chapter 9-1c2 Practice Project Status: Complete

# A program that creates a dictionary, provides a menu of choices to the user,
# and can display the entire dictionary. There will be 4 different modules,
# with the main program importing all the modules.
# Module 3, add and show_all modules.

# Global constants set from menu.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
SAVE = 6
RETRIEVE = 7
QUIT = 8


# Add function.
def add(cats):
    name = input('Enter a cat name: ')
    type = input('Enter a cat type: ')

    # Seeing if name already exists, or adding new name to dictionary.
    if name not in cats:
        cats[name] = type
    else:
        print('That entry already exists.')


# Show all function to show the entire dictionary.
def show_all(cats):
    print(cats)
