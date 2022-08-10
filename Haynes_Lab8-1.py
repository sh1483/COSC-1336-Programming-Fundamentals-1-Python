# Name: Steven Haynes
# Lab 8-1 Project Status: Complete

# A program that reads text.txt and determines: The number of uppercase letters,
# the number of lowercase letters, the number of digits, and the number of
# whitespace characters in the file.

def main():

    # Open text.txt in read only.
    infile = open('text.txt', 'r')

    # Create empty count holders.
    count_upper = 0
    count_lower = 0
    count_digits = 0
    count_whitespace = 0

    # Read the text.txt file.
    text = infile.read()

    # Count case, digits, and whitespace.
    for ch in text:
        if ch.isupper():
            count_upper += 1
        if ch.islower():
            count_lower += 1
        if ch.isdigit():
            count_digits += 1
        if ch.isspace():
            count_whitespace += 1

    # Print out results.
    print('Uppercase letters: ', count_upper)
    print('Lowercase letters: ', count_lower)
    print('Digits: ', count_digits)
    print('Spaces: ', count_whitespace)

    # Close the text.txt file.
    infile.close()


main()
