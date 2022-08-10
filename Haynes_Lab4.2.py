# Steven Haynes
# Lab 4.2 Status: Complete

# A program that calculates the oceans rise, in millimeters,
# over the next 25 years.

year_count = 0

# Start the heading
print('Year\tRise (in millimeters)')
print('---------------------------')

# Set a constant amount of rise in sea level
RISE = 1.8

# Create a count to 25, and display the corresponding rise (tabbed over).

for number in range(1, 26):
    annual_rise = number * RISE
    print(number, '\t', format(float(annual_rise), '.2f'))
