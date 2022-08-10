# Name: Steven Haynes
# Chapter 6-3 Practice Project Status: Complete

# A program that creates students.txt, reads in records using a loop,
# then displays the records using a loop.

def main():

    another = 'y'

    students_file = open('students.txt', 'a')

    while another == 'y' or another == 'Y':

        student = input("Enter the student's name: ")
        grade = float(input("Enter the student's exam grade: "))

        students_file.write(student + '\n')
        students_file.write(str(grade) + '\n')

        print('Do you want to input another name and grade?')

        another = input('Y = yes, anything else = no: ')

    students_file.close()

    students_file = open('students.txt', 'r')

    print('\n')
    print('Name' + '\tScore')
    print('_________________')

    name = students_file.readline()

    while name != '':
        score = float(students_file.readline())
        name = name.rstrip('\n')

        print(name, '\t\t', score)

        name = students_file.readline()

    students_file.close()


main()
