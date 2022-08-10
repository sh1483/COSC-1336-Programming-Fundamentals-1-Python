# Name: Steven Haynes
# Chapter 6-2a Practice Project Status: Complete

# A program that opens an output file named number_list.txt.
# Uses a loop to write the numbers 50-100 to the .txt file
# , then closes the file.


def main():
    outfile = open('number_list.txt', 'w')

    for count in range(50, 101):
        outfile.write(str(count) + '\n')

    outfile.close()


main()
