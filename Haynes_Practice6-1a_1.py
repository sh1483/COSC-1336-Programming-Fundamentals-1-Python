# Name: Steven Haynes
# Chapter 6-1A Practice Project Status: Complete

# A program that opens an output file (my_name.txt), writes my name and someone
# else's name, and writes my age to the file.

def main():

    name1 = 'Steven Haynes'
    name2 = 'Kristen Starzynski'

    age = 38

    name_file = open('my_name.txt', 'w')

    name_file.write(name1 + '\n')
    name_file.write(name2 + '\n')
    name_file.write(str(age) + '\n')

    name_file.close()


main()
