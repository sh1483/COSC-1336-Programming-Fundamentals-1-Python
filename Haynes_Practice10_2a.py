# Name: Steven Haynes
# Chapter 10-2a Practice Project Status: Complete

# A program that creates a class names Pet with the following attributes:
# __name, __animal_type, and __age. It has the following methods:
# __init__, set_name, set_animal_type, set_age, get_name, get_animal_type,
# and get_age.
# A Second program will create an object of the class and prompt a user
# to enter: name, type, and age of their pet(s).
# This will be stored as attributes. The object attributes will be retrieved
# with accessor methods and displayed.

# Create the class.
class Pet:

    # Initialize method that creates attributes.
    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    # Method to assign name.
    def set_name(self, name):
        self.__name = name

    # Method to assign type.
    def set_animal_type(self, type):
        self.__animal_type = type

    # Method to assign age.
    def set_age(self, age):
        self.__age = age

    # Method to return the name.
    def get_name(self):
        return self.__name

    # Method to return the type.
    def get_animal_type(self):
        return self.__animal_type

    # Method to return the age.
    def get_age(self):
        return self.__age
