# Name: Steven Haynes
# Lab 6.8 Project Status: Complete

# A program that reads the random_number.txt file,
# displays the numbers, then displays the total number of numbers,
# and the total of the numbers. MUST CONTAIN EXCEPTIONS.

def main():
    # Read in the file.
    infile = open('random_number.txt', 'r')

    # Set an accumulator for the sum of the numbers.
    total = 0.0
    # Set the total count of the numbers.
    count = 0

    # Account for exceptions
    try:

        # Create a loop that returns the numbers in random_number.txt
        for line in infile:
            number = int(line)
            print(number)

            # Determine the count.
            num_sum = int(line)
            count += 1

            # Determine the sum.
            total += num_sum

        print('Total:', total)
        print('Count:', count)

    except ValueError:

        print('ERROR: must use valid numbers.')

    except IOError:

        print('ERROR, could not read file.')

    except:

        print('An error occurred.')

    infile.close()


main()
