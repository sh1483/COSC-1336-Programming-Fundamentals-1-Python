# Name: Steven Haynes
# Chapter 4-1b Project Status: Complete

# A while loop asking the user for 2 numbers, then summing them. A loop
# allows the user to continue if desired.

go_again = 'y'

while go_again == 'y':

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))

    total = num1 + num2

    print("Those numbers add up to: ", format(float(total), ',.2f'))

    go_again = input("Go again? 'y' for yes: ")
