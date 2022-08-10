# Name: Steven Haynes
# Chapter 9 Lab Project Status: Complete

# A program that creates a dictionary with course number and room numbers the
# courses meet in. Creates another dictionary with course numbers and
# corresponding instructors. A third dictionary with course numbers and
# meet times. If a course is not in the dictionary a message will display.
# Program contains a loop asking user for course number until they want to quit.


def main():

    # Create course & room dictionary.
    course_room = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755',
                   'NT110': '1244', 'CM241': '1411'}

    # Create course & instructor dictionary.
    course_instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado',
                         'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}

    # Create course & time dictionary.
    course_time = {'CS101': '8:00 am', 'CS102': '9:00 am', 'CS103': '10:00 am',
                   'NT110': '11:00 am', 'CM241': '1:00 pm'}

    # Set again to yes.
    again = 'y'

    # Create a loop using again.
    while again.lower() == 'y':

        # Have user input a course number to search.
        choice = input('Enter a course number: ')

        # Test course number is in a dictionary.
        if choice.upper() in course_room:

            # Return course, room, instructor, and time. Formatted.
            print('Course Number:', choice.upper(), '\nRoom Number: ',
                  course_room.get(choice.upper(), 'Course Number not valid.'),
                  '\nInstructor:',
                  course_instructor.get(choice.upper(), 'Course Number not valid.'),
                  '\nTime:',
                  course_time.get(choice.upper(), 'Course Number not valid.'))
        else:
            # If test is false, error message.
            print('Invalid Course Name')

        # Check to see if loop will run again.
        print()
        print('Do you want to check another course?')
        again = input('y = yes, anything else = no: ')

        print()


main()
