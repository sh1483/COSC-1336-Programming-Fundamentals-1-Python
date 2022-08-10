# Name: Steven Haynes
# Chapter 7B-3 Practice Project Status: Complete

# A program that contains a main function and a sub-function called total_list.
# The main function creates 2 lists of 5 integers each.
# The main function will join the 2 lists, sort the resulting 10 integers,
# and pass it to the total_list function.
# The total_list function will total the integers in the list,
# and return it to main. Main will print the list, the total,
# and the min and max values in the list.

def main():

    list1 = [1, 2, 3, 4, 5]
    list2 = [11, 12, 13, 14, 15]

    list3 = list1 + list2

    list3.sort()

    print('The list contains the following numbers:', list3)
    print('The total of the numbers in the list is: ', total_list(list3))
    print('The smallest number in the list is: ', min(list3))
    print('The largest number in the list is: ', max(list3))


def total_list(value_list):
    total = 0
    for num in value_list:
        total += num

    return total


main()
