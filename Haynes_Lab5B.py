# Name: Steven Haynes
# Lab 5B Status: In-Progress

# A program that calculates the distance in meters based
# on an object's falling distance. The program uses 2 functions:
# main and falling_distance.

import distance


def main():

    # Creating the header.
    print("Time" "\tFalling Distance")
    print("________________________")

    # A loop, passed the values 1-10 as arguments.
    for time in range(1, 11):

        print(time, '\t', format(float(distance.falling_distance(time)), ',.2f'))


main()
