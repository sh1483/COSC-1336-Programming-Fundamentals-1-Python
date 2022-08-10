# Name: Steven Haynes
# Chapter 6-4 Practice Project Status: In Progress

# A program that opens number_list.txt,
# and calculates the sum and average of the numbers.

def main():
    infile = open('random_number.txt', 'r')

    # Set an accumulator for the sum of the numbers.
    total = 0.0
    # Set the total count of the numbers.
    count = 0

    try:

        for line in infile:
            num_sum = int(line)
            count += 1

            total += num_sum

        print(total)

        average = (total / count)
        print(average)
    except ValueError:

        print('ERROR: must use valid numbers.')

    except IOError:

        print('ERROR, could not read file.')

    except:

        print('An error occurred.')

    infile.close()


main()
