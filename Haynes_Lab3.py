# Steven Haynes
# Lab 3 Status: Complete

# A program that takes users software package purchase input and determines
# pricing based off of a table.

# Determine the number of desired packages.
packages = int(input('Type requested number of software packages: '))

# Set the base price of a single package.
BASE_PRICE = 149.00

# Discount does not apply to purchase of fewer than 10 packages.
if packages < 10:
    discount = format(float((BASE_PRICE * packages) * 0.0))


# 10% discount applies for 10-49 packages. Return the dollar value of
# the discount.
elif 10 <= packages <= 49:
    discount = format(float((BASE_PRICE * packages) * 0.1))


# 20% discount for 50-99 packages. Return dollar value.
elif 50 <= packages <= 99:
    discount = format(float((packages * BASE_PRICE) * 0.2))


# 30% off for 100-149 packages. Return dollar value.
elif 100 <= packages <= 149:
    discount = format(float((packages * BASE_PRICE) * 0.3))


# 40% off for 150+ packages. Return dollar value.
else:
    discount = format(float((packages * BASE_PRICE) * 0.4))
print("You earned $", format(float(discount), ',.2f'), "off!")

# Total price is number of packages * 149, minus the discount.
total_price = (packages * BASE_PRICE) - float(discount)

# Return the total price after applying discounts.
print("Your total comes out to: $", format(float(total_price), ',.2f'))
