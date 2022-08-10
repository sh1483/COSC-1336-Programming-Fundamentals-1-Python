# Name: Steven Haynes
# Chapter 6-2b Practice Project Status: Complete

# A program that opens number_list.txt, and prints the numbers.
# Uses a for loop to terminate at the end of the file.

def main():
    infile = open('number_list.txt', 'r')

    for line in infile:
        number = int(line)
        print(number)

    infile.close()


main()
