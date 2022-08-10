# Name: Steven Haynes
# Lab 6.7 Project Status: In Progress

# A program that writes a series of random numbers, 1-500, to a file.
# A user specifies how many random numbers the file will hold.
# MUST USE EXCEPTIONS. THIS FILE WORKED PERFECTLY BEFORE USING EXCEPTIONS.

import random


def main():

    # open the file random_number.txt
    outfile = open('random_number.txt', 'w')

    # Create exception clauses.
    try:

        # Have user input a number 1-500.
        choice = int(input('Enter the max number you want'
                               ' in your file (1-500): '))

        # Ensure choice is between 1 and 500.
        if choice not in range(1, 501):

            choice = int(input('Enter the max number you want'
                                   ' in your file (1-500): '))

            # Loop through the numbers in the range.
            for count in range(choice):
                outfile.write(str(random.randrange(1, 501)) + '\n')

    except IOError:

        print('ERROR!')

    except ValueError:

        print('ERROR! Must use a valid integer.')

    except:
        print('An error occurred.')

    outfile.close()


main()
