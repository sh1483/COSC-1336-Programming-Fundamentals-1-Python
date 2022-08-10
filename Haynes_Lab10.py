# Name: Steven Haynes
# Chapter 10 Lab Project Status: Complete

# A main program that creates three instances of the Employee class, using
# user input. The __str__ method will be invoked by a print function that
# displays the Employee information for the three employees.

# Imports the class from a file.
import employee


# Create the main program.
def main():

    # Get a list of employee objects.
    employees = make_list()
    # Display the data in the list.
    display_list(employees)


# Get data from the user for 3 employees.
def make_list():
    # Create an empty list.
    employees_list = []

    # Add 3 employee objects to the list.
    for count in range(1, 4):
        number = str(count)
        name = input("Enter the employee's Name: ")
        idnum = input("Enter the employee's ID Number: ")
        dept = input("Enter the employee's Department: ")
        title = input("Enter the employee's Job Title: ")
        print()

        # Create a new Employee object and assign it to employee1.
        employees = employee.Employee(number, name, idnum, dept, title)

        # Add the object to the list.
        employees_list.append(employees)

    # Return the list
    return employees_list


# A function that accepts a list with Employee objects as an argument and
# shows the stored data.
def display_list(employees_list):
    for employees in employees_list:

        # Display the employee information.
        print(employees)
        print()


# Call the main.
main()
