# Name: Steven Haynes
# Chapter 5A-1 Practice Project Status: Complete

# A program to display the steps of making a sandwich.

print('Hi! This is how you can make a turkey sandwich.')


# Defining the main function
def main():
    input("Press 'Enter' if you are ready to begin.")
    print()
    supplies_list()
    print()
    input("Press 'Enter' to see Step 1.")
    step1()
    input("Press 'Enter' to see Step 2.")
    step2()
    input("Press 'Enter' to see Step 3.")
    step3()
    input("Press 'Enter' to see Step 4.")
    step4()
    input("Press 'Enter' to see Step 5.")
    step5()
    input("Press 'Enter' to see Step 6.")
    step6()


# Defining the steps.
def supplies_list():
    print("You need the following supplies: a plate, a knife, "
          "2 slices of bread, 6 slices of turkey, a slice of cheese,"
          " mayonnaise, and mustard.")


def step1():
    print("Step 1: Place the slices of bread beside each other on the plate.")
    print()


def step2():
    print("Step 2: Using the knife, spread mayonnaise on top"
          " of both slices of bread.")
    print()


def step3():
    print("Step 3: Stack the turkey slices on top of the piece of"
          " bread on the left.")
    print()


def step4():
    print("Step 4: Place the cheese slice on top of the slice"
          " of bread on the right.")
    print()


def step5():
    print("Step 5: Place the right slice of bread, cheese side down,"
          " on top of the slice of bread on the left. "
          "The turkey and cheese should be touching.")
    print()


def step6():
    print("Enjoy your turkey sandwich!")


# Calling the main function.
main()
