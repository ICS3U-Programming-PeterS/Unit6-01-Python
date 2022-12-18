#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Dec 16, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the average to the console

import constants
import random


def main():
    # initializing sum and counter
    sum = 0
    counter = 0

    # making empty list
    list_of_ints = []

    # displays random numbers and calculates average
    for counter in range(constants.MAX_ARRAY_SIZE):
        list_of_ints.append(random.randint(constants.MIN_NUM,
                                           constants.MAX_NUM))
        sum = sum + list_of_ints[counter]
        if list_of_ints[counter] < 10:
            print(f"{list_of_ints[counter]}  added to the" +
                  " list at position {counter}")
        else:
            print(f"{list_of_ints[counter]} added to the" +
                  " list at position {counter}")

    # calculate and display average
    average = sum / constants.MAX_ARRAY_SIZE
    print(f"\nThe average is {average}")


if __name__ == "__main__":
    main()
