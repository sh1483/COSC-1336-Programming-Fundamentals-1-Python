# Name: Steven Haynes
# Chapter 4-3 Practice Project Status: Complete

# A program that: Asks a user for a positive integer <= 15,
# using input validation. Asks for a character. Displays a square on the screen
# that is the input number of rows and columns wide and tall,
# made of the provided character.

# Ask for a positive integer 0-15.

rows = int(input('Enter an integer 1-15: '))
while rows < 1 or rows > 15:
    rows = int(input('Error: Enter a POSITIVE INTEGER 1-15: '))

# Ask for a character.
symbol = input('Enter any character: ')

cols = rows

for r in range(rows):
    for c in range(cols):
        print(symbol, end='')
    print()
