# Name: Steven Haynes
# Project Status: Complete

# A program to determine the serving size needed and returning the amount of
# required ingredients for the serving size.


# Taking given serving size and dividing to get a single serving size.
cups_tomato_sauce = 2/4
cups_tomato_paste = .333/4
cloves_garlic = 2/4
tbsp_oregano = 1/4

# Taking user input on serving size, to accommodate decimals.
servings = float(input("How many servings of Spaghetti Sauce do you need?"))

# Multiplying given input by a single serving size.
needed_tomato_sauce = (cups_tomato_sauce * servings)
needed_tomato_paste = (cups_tomato_paste * servings)
needed_garlic = (cloves_garlic * servings)
needed_oregano = (tbsp_oregano * servings)

# Providing a return.
# Could not figure out how to format as one print function without a space
# before the number of cups of tomato sauce needed. Wrote two print functions
# to make it look how I wanted it to look.
print("You need:")
print(format(needed_tomato_sauce, '.2f'), "cups of tomato sauce")
print(format(needed_tomato_paste, '.2f'), 'cups of tomato paste')
print(format(needed_garlic, '.2f'), 'cloves of garlic')
print(format(needed_oregano, '.2f'), 'Tablespoons of oregano')

