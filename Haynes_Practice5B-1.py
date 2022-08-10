# Name: Steven Haynes
# Chapter 5B-1 Practice Project Status: Complete

# A program that generates random float point numbers 1-100,
# used as the radius of a circle. A separate function calculates the area
# of a circle based on the randomly generated radius.

# Importing the random library
import random


# Setting a range for the radius to be between 1 and 100.
MIN = 1.0
MAX = 101.0

# Get a random number.
number = random.uniform(MIN, MAX)


def main():

    #Getting the area.
    area = get_area()

    print('The random radius is', number,
          'and the area of the circle with that radius is', area)


# Defining the area.
def get_area():
    area = 3.14 * (number**2)
    return area


main()
