# Name: Steven Haynes
# Lab 7 Project Status: Complete

# A program that has a main function which accepts input of a series of
# 10 integers, as well as an integer n that is the search number.
# Main calls the function display_larger and passes 2 arguments:
# the list of 10 integers, and the number n.
# The function display_larger accepts 2 parameters from main.
# Uses a loop to compare all numbers in the list to the number n.
# Creates a second list for all numbers larger than n.
# Then displays the original list, n, and the list of numbers greater than n.

# Constant for list length.
LIST_LENGTH = 10


def main():

    # Assign accumulator values to list1
    list1 = [0] * LIST_LENGTH
    index = 0

    print('You will enter a list of 10 integers.')

    # A loop to get user input for list1.
    while index < len(list1):
        list1[index] = int(input('Enter an integer: '))
        index += 1

    # Getting input for n.
    n = int(input("Enter the number you wish to test if the"
            " list elements are greater than: "))

    # Call display_larger and pass list1 and n.
    display_larger(list1, n)


def display_larger(list1, n):

    # Create empty list2 for accumulator.
    list2 = []

    # Determine if numbers in list1 are larger than n.
    for item in list1:
        if item > n:
            # Add numbers larger than n to list2.
            list2.append(item)

        # Printing out n.
    print('\n', 'Number: ', n, '\n')
    # Print out list1.
    print('The list of numbers: ', '\n', list1, '\n')
    # Print out numbers larger than n.
    print('The list of numbers larger than', n, ':', '\n', list2)


main()
