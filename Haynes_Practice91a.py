# Name: Steven Haynes
# Chapter 9-1 Practice Project Status: Complete

# A program that creates a dictionary, provides a menu of choices to the user,
# and can display the entire dictionary. There will be 4 different modules,
# with the main program importing all the modules. Module 1, main module.

# Import the other modules.
import Haynes_Practice91b
import Haynes_Practice91c
import Haynes_Practice91d


# Set global constants.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
QUIT = 6


def main():
    # Create a dictionary.
    cats = {'Pablo': 'Tiger', 'Mario': 'Puma'}

    # Create an accumulator
    choice = 0

    # Coordinates other programs through the menu.
    while choice != QUIT:
        choice = Haynes_Practice91b.get_menu_choice()
        if choice == Haynes_Practice91b.LOOK_UP:
            Haynes_Practice91b.look_up(cats)
        elif choice == Haynes_Practice91c.ADD:
            Haynes_Practice91c.add(cats)
        elif choice == Haynes_Practice91d.CHANGE:
            Haynes_Practice91d.change(cats)
        elif choice == Haynes_Practice91c.SHOW_ALL:
            Haynes_Practice91c.show_all(cats)
        elif choice == Haynes_Practice91d.DELETE:
            Haynes_Practice91d.delete(cats)


main()
