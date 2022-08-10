# Name: Steven Haynes
# Lab 5A Status: Complete

# A program that accepts input of five numeric ratings USING A LOOP.
# Then calculates the average score, passed to the determine_stars function.
# The determine_stars function displays *'s based on number rating.

MAX = 5


def main():
    # Calculate a running total that adds 5 input numbers.

    accumulated_score = 0.0

    for counter in range(MAX):
        score = float(input('Enter a score 0-10: '))
        while score not in range(0, 11):
            score = float(input('Error. Enter number 0-10: '))
        accumulated_score += score

    # Average the accumulated_score function
    average_score = accumulated_score/MAX

    print("The restaurant scored a ", format(float(average_score), ',.2f'))
    print("For a star rating of: ", determine_stars(average_score))


def determine_stars(numeric_average):
    # Create a star classification for the numeric_average function.

    if numeric_average > 9:
        star_rating = '*****'

    elif 8.9 <= numeric_average or numeric_average >= 8.0:
        star_rating = '****'

    elif 7.9 <= numeric_average or numeric_average >= 7.0:
        star_rating = '***'

    elif 6.9 <= numeric_average or numeric_average >= 6.0:
        star_rating = '**'

    elif 5.9 <= numeric_average or numeric_average >= 5.0:
        star_rating = '*'

    else:
        star_rating = 'No stars'

    return star_rating


main()
