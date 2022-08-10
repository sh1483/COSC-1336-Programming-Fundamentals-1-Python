# Name: Steven Haynes
# Chapter 5A-2 Practice Project Status: Complete

# A program to convert user input kilometers to miles.

MAGIC = 0.6214

def main():

    # Get the number of kilometers.
    kilometers_needed = int(input("Enter the number of kilometers: "))

    # Convert the kilometers to miles.
    kilometers_to_miles(kilometers_needed)


# The kilometers_to_miles function accepts a number of kilometers
# and converts to miles.
def kilometers_to_miles(kilometers):

    MILES = kilometers * MAGIC
    print('That converts to', format(float(MILES), ',.2f'), 'miles.')


main()
