# Name: Steven Haynes
# Chapter 8-1 Practice Project Status: Complete

# A program that accepts input of first, middle and last names
# in 3 separate strings. Concatenates them into a string called full_name.
# Counts the number of Aa's, Ee's, and Ss's, and displays each
# of the three counts.


def main():

    # Empty counts created
    count_a = 0
    count_e = 0
    count_s = 0
    # User input for name.
    first_name = input('Enter your first name: ')
    middle_name = input('Enter your middle name: ')
    last_name = input('Enter your last name: ')

    # Concatenate name strings into one.
    full_name = first_name + ' ' + middle_name + ' ' + last_name

    # Test for and count Aa's, Ee's, Ss's.
    for ch in full_name:
        if ch == 'A' or ch == 'a':
            count_a += 1
        if ch == 'E' or ch == 'e':
            count_e += 1
        if ch == 'S' or ch == 's':
            count_s += 1

    # Print results
    print('The letter "A" appears', count_a, 'times.')
    print('The letter "E" appears', count_e, 'times.')
    print('The letter "S" appears', count_s, 'times.')


main()
