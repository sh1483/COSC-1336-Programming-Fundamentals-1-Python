# Name: Steven Haynes
# Chapter 10 Lab Project Status: Complete

# A program that creates a class named Employee that holds the following data:
# name, idnum number, Department, and Job Title. The class will include:
# an initializer method, setter and getter methods for each attribute,
# and a __str__ method to print the contents of the class.
# A main program will create three instances of the Employee class, using
# user input. The __str__ method will be invoked by a print function that
# displays the Employee information for the three employees.

class Employee:

    # Initialize method that creates attributes.
    def __init__(self, number, name, idnum, dept, title):
        self.__number = number
        self.__name = name
        self.__idnum = idnum
        self.__dept = dept
        self.__title = title

    # Method to assign number.
    def set_number(self, number):
        self.__number = number

    # Method to assign name.
    def set_name(self, name):
        self.__name = name

    # Method to assign idnum.
    def set_idnum(self, idnum):
        self.__idnum = idnum

    # Method to assign department.
    def set_department(self, dept):
        self.__dept = dept

    # Method to assign job title.
    def set_title(self, title):
        self.__title = title

    # Method to return the number.
    def get_number(self):
        return self.__number

    # Method to return the name.
    def get_name(self):
        return self.__name

    # Method to return the idnum number.
    def get_idnum(self):
        return self.__idnum

    # Method to return the department.
    def get_dept(self):
        return self.__dept

    # Method to return the job title.
    def get_title(self):
        return self.__title

    # Method to return a string.
    def __str__(self):
        return "Employee Number " + self.__number + "\nName: " + self.__name +\
               "\nID Number: " + self.__idnum + "\nDepartment: " + self.__dept\
               + "\nJob Title: " + self.__title
