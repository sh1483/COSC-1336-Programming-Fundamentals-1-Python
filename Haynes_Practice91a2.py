# Name: Steven Haynes
# Chapter 9-1a2 Practice Project Status: Complete

# A program that creates a dictionary, provides a menu of choices to the user,
# and can display the entire dictionary. There will be 4 different modules,
# with the main program importing all the modules. Module 1, main module.

# Import the other modules.
import Haynes_Practice91b2
import Haynes_Practice91c2
import Haynes_Practice91d2
import Haynes_Practice92


# Set global constants.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
SAVE = 6
RETRIEVE = 7
QUIT = 8


def main():
    # Create a dictionary.
    cats = {'Pablo': 'Tiger', 'Mario': 'Puma'}

    # Create an accumulator
    choice = 0

    # Coordinates other programs through the menu.
    while choice != QUIT:
        choice = Haynes_Practice91b2.get_menu_choice()
        if choice == Haynes_Practice91b2.LOOK_UP:
            Haynes_Practice91b2.look_up(cats)
        elif choice == Haynes_Practice91c2.ADD:
            Haynes_Practice91c2.add(cats)
        elif choice == Haynes_Practice91d2.CHANGE:
            Haynes_Practice91d2.change(cats)
        elif choice == Haynes_Practice91c2.SHOW_ALL:
            Haynes_Practice91c2.show_all(cats)
        elif choice == Haynes_Practice91d2.DELETE:
            Haynes_Practice91d2.delete(cats)
        elif choice == Haynes_Practice92.SAVE:
            Haynes_Practice92.save(cats)
        elif choice == Haynes_Practice92.RETRIEVE:
            Haynes_Practice92.retrieve(cats)


main()
