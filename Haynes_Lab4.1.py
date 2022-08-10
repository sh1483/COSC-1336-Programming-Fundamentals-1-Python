# Steven Haynes
# Lab 4.1 Status: Complete

# A program that takes a users monthly budget, asks for expenses,
# and returns an amount stating if over or under budget.


# Determine the initial budget.
budget = float(input('Enter amount budgeted for the month: '))

# Set accumulator total to zero.
total = 0

# Determine expenses, with option to stop.
expense = float(input('Enter an amount spent (0 to quit): '))

while expense != 0.0:
    expense = float(input('Enter an amount spent (0 to quit): '))

# Calculate the expenses.
    total = total + expense

# Determine if over or under budget and respond accordingly.
if total > budget:
    print('You budgeted: $', format(float(budget), ',.2f'))
    print('You spent: $ ', format(float(total), ',.2f'))
    print('You are $', format(float(total - budget), ',.2f'),
          ' OVER budget!')

else:
    print('You are $ ', format(float(budget - total), ',.2f'),
          ' UNDER budget!')
