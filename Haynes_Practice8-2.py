# Name: Steven Haynes
# Chapter 8-2 Practice Project Status: Complete

# A program that accepts input of a sentence that contains upper & lower case,
# as well as special characters. Creates a new string where all the
# lower case become upper and all the upper case become lower.
# Prints the original and the new sentence.

# Create a global for special characters that are acceptable.
spec_char = '!@#$%^&*()-+?_=,<>/'


# Get input of a string.
def main():
    first_sentence = input('Type a sentence with upper and lower case letters, '
                           'and at least one'
                           ' special character (!@#$%^&*()-+?_=,<>/): ')

    # Create an empty string.
    new_sentence = ''

    while not valid_sentence(first_sentence):
        print('That sentence is not valid.')

        first_sentence = input('Type a sentence with upper and lower case letters, '
                               'and at least one'
                               ' special character (!@#$%^&*()-+?_=,<>/): ')

    # Test and add flipped characters.
    for ch in first_sentence:
        if ch.isupper() == True:
            new_sentence += ch.lower()

        elif ch.islower() == True:
            new_sentence += ch.upper()

        elif ch in spec_char:
            new_sentence += ch

    # Print original and new strings.
    print(first_sentence, '\n', new_sentence)


# Create valid sentence.
def valid_sentence(sentence):
    # Set validity to False.
    has_uppercase = False
    has_lowercase = False
    has_spec_char = False

    # Ensure string meets validity requirements.
    for ch in sentence:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch in spec_char:
            has_spec_char = True

    # Make string valid or invalid.
    if has_uppercase and has_lowercase and has_spec_char:
        is_valid = True
    else:
        is_valid = False

    return is_valid


main()
