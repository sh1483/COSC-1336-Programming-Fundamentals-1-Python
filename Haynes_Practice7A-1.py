# Name: Steven Haynes
# Chapter 7A-1 Practice Project Status: Complete

# A program that generates a 7 digit lottery number, using a loop and random,
# within the range 0-9, adn assigns each number to a list element.
# Uses another loop to display the contents of the list.

import random

# Set a constant for the number of digits in the lottery number.
DIGITS = 7


def main():

    # Create the initial lottery number of 7 zeros.
    lotto_number = [0] * DIGITS
    print(lotto_number)
    index = 0

    # A loop to randomly assign numbers 0-9 to each element of
    # the lotto_number list
    while index < len(lotto_number):
        lotto_number[index] = random.randint(0, 9)
        index += 1

    # A loop that returns each new value for the lotto_number list.
    for value in lotto_number:
        print(value)

    # Printing out the new lotto_number list.
    print(lotto_number)


main()
