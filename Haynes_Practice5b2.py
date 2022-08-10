# Name: Steven Haynes
# Chapter 5B-2 Practice Project Status: Complete

# A program that calculates the area of a square based on
# a randomly generated integer which will represent the length and width.

import random
import square


def main():

    side = random.randrange(1, 101)

    print('side:', side, '\t\tarea:', square.square_area(side), '\tperimeter:',
          square.square_perimeter(side), sep='')


main()
