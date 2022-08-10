# Name: Steven Haynes
# Chapter 7B-4 Practice Project Status: Complete

# A program that creates a two-dimensional list with 4 rows and 3 columns.
# A nested loop will get integer values from the user for each element
# in the list. Another nested loop will sum and display each element
# in the list, and the total of the elements will be found and printed.

# Constants for rows and columns.
ROWS = 4
COLS = 3


def main():

    # Create a two-dimensional list.
    values = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    # User fills the list with input numbers.
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = int(input('Enter an integer: '))

    # Returning the values.
    print(values)

    # Setting an accumulator.
    total = 0

    # Nested loop to total the numbers in the list.
    for r in range(ROWS):
        for c in range(COLS):
            total += values[r][c]

    print('The total of all your numbers is: ', total)


main()
