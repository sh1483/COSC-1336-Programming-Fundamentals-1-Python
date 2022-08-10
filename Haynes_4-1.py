# Name: Steven Haynes
# Chapter 4-1 Project Status: Complete

# A program that asks the user for a number, 1-7, and returns the
# corresponding day of the week using if-elif-else. Then used a while statement
# to loop until user is ready to stop.

# A variable to control the loop.
keep_going = 'y'

while keep_going == 'y':

# Seeking user input 1-7.
        day = int(input("Enter a number 1-7: "))

# Assigning a day to a number.
        if day == 1:
            print('Monday')

        elif day == 2:
            print('Tuesday')

        elif day == 3:
            print('Wednesday')

        elif day == 4:
            print('Thursday')

        elif day == 5:
            print('Friday')

        elif day == 6:
            print('Saturday')

        elif day == 7:
            print('Sunday')

# Assigning an error if number is not 1-7.
        elif day != range(1,8):
            print('Error, number not 1-7!')

# Providing the user an out from the loop.
        keep_going = input('Do you want to continue? (Enter y for yes): ')
