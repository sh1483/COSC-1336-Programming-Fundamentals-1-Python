# Steven Haynes
# Ch. 3-1 Practice Status: Complete

# A program that uses input to determine if a date is a "magic number",
# where the month times the day equals the year.

# Asking user to input integers.
month = int(input('Enter a month in numeric form: '))
day = int(input("Enter a day 1-31: "))
year = int(input("Enter a 2 digit year: "))

# Multiplying the month by the day to see if it equals the year,
# and is thus a magic date.

if (month * day) == year:
    print("This is a magic date!")

else:
    print("This date is not magic.")
