# Name: Steven Haynes
# Chapter 6-1B Practice Project Status: Complete

# program that opens my_name.txt then reads and displays the names.
# It then reads my age, and divides it by 2.
# Then prints the original age and the age divided by 2.


def main():
    infile = open('my_name.txt', 'r')

    my_name = infile.readline()
    my_name = my_name.rstrip('\n')

    her_name = infile.readline()
    her_name = her_name.rstrip('\n')

    my_age = infile.readline()
    my_age = int(my_age.rstrip('\n'))

    half_age = my_age/2

    infile.close()

    print('The names are:', my_name, '&', her_name)
    print('My age is:', my_age, 'and half my age is:', half_age)


main()
