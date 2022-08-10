# Name: Steven Haynes
# Chapter 9-2 Practice Project Status: In Progress

# A program that adds to 9-1, pickles the dictionary to a file,
# retrieves the saved pickled file,
# all within a separate module that is imported and used by 9-1.

import pickle


# Set global constants.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
SAVE = 6
RETRIEVE = 7
QUIT = 8


def save(cats):
    save = open('cats.dat', 'wb')
    pickle.dump(cats, save)
    save.close()
    print("Saved to cats.dat")


def retrieve(cats):
    retrieve = open('cats.dat', 'rb')
    pb = pickle.load(retrieve)
    print(pb)
    retrieve.close()
