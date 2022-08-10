# A program that ask the user for a number, 1-7, and returns the
# corresponding day of the week using if-else-if.

day = int(input("Enter a number 1-7: "))

if day == 1:
    print('Monday')

else:

    if day == 2:
        print('Tuesday')

    else:

        if day == 3:
            print('Wednesday')

        else:

            if day == 4:
                print('Thursday')

            else:

                if day == 5:
                    print('Friday')

                else:

                    if day == 6:
                        print('Saturday')

                    else:

                        if day == 7:
                            print('Sunday')

                        else:

                            if day >= 8:
                                print('Error, number is not 1-7!')

