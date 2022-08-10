# Name: Steven Haynes
# Lab 8-2 Project Status: Complete

# A program that reads a user input string in date form mm/dd/yyyy and then,
# creates a copy of the string formatted to long month dd, yyyy format,
# and returns that.

# I am sure there is a more efficient way to do this
# with count and range, probably. I just find this more time efficient within
# my current skill set since I don't have to research and
# trial and error it out... maybe if I have time this weekend
# I will give it a shot.

def main():

    # Get a user input date.
    short_date = input('Enter a date in the format mm/dd/yyy: ')

    # Convert to a list, stripping the /.
    date_list = short_date.split('/')

    # Set month from numerical to month name.
    if '01' == date_list[0]:
        month = 'January'
    elif '02' == date_list[0]:
        month = 'February'
    elif '03' == date_list[0]:
        month = 'March'
    elif '04' == date_list[0]:
        month = 'April'
    elif date_list[0] == '05':
        month = 'May'
    elif date_list[0] == '06':
        month = 'June'
    elif date_list[0] == '07':
        month = 'July'
    elif date_list[0] == '08':
        month = 'August'
    elif date_list[0] == '09':
        month = 'September'
    elif date_list[0] == '010':
        month = 'October'
    elif date_list[0] == '11':
        month = 'November'
    else:
        month = 'December'

    # Print month name, day + comma, and year.
    print(month, date_list[1] + ',', date_list[2])


main()
