# Name: Steven Haynes
# Chapter 4-1 Project Status: Complete

# A program that asks the user for a number, 1-7, and returns the
# corresponding day of the week using if-elif-else.


day = int(input("Enter a number 1-7"))


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

else:
    print('Error, number not 1-7!')


