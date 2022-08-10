# Name: Steven Haynes
# Chapter 10-2b Practice Project Status: Complete

# A program that creates an object of the Pet class and prompts a user
# to enter: name, type, and age of their pet(s).
# This will be stored as attributes. The object attributes will be retrieved
# with accessor methods and displayed.

# Imports the class from a file.
import Haynes_Practice10_2a


def main():

    # Get user input for name, type and age of the pet.
    name = input("Enter the pet's name: ")
    type = input('Enter the type of animal: ')
    age = input("Enter the pet's age: ")

    # Create an instance of the Pet class.
    pet = Haynes_Practice10_2a.Pet(name, type, age)

    # Display the data that was entered.
    print('Here is the data you have entered: ')

    # Using the getters to retrieve name, type and age.
    print('Name:', pet.get_name())
    print('Animal Type:', pet.get_animal_type())
    print('Age:', pet.get_age())


# Call the main function.
main()
