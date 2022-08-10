# Steven Haynes
# Program Status: Complete

# Asking a user to input product prices, then printing a total
# and an average price.

# Write 3 input statements asking for user input on prices.
hamburgerPrice = float(input('How much for a burger? '))
friesPrice = float(input('What does it cost for fries? '))
shakePrice = float(input('And what about the price of a shake? '))

# Provide a total price.
totalPrice =hamburgerPrice + friesPrice + shakePrice
print('The total comes out to: $ ', totalPrice)

#Provide an average price (amount of decimals doesn't matter for cents)
averageCost = (hamburgerPrice + friesPrice + shakePrice) /3
print('The average product price is: $ ', averageCost)
