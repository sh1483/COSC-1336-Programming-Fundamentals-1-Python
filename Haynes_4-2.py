# Name: Steven Haynes
# Chapter 4-2 Project Status: Complete

# A program where the user inputs upper and lower boundaries. The iterator
# will be displayed, as well as factor of 10 of the iterator,
# separated by a tab. A second loop will accumulate between the upper and
# lower limits.

# Tell the user what is going on.
print('This program requires you to input 2 numbers, '
      'a low number and a high number')

# Have user input high and low numbers.
start = int(input('Enter your low integer: '))
stop = int(input('Enter your high integer: '))

# Set accumulator total to zero.
total = 0

# Find the numbers in the user set range, print them plus the multiplier.
for number in range(start, stop + 1):
    print(number, '\t', number * 10)

# Add the running total of the numbers in the set range.
for number in range(start, stop + 1):
    total = total + number

# Show the running total.
print(total)

