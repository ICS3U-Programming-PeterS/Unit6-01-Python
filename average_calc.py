#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Dec 16, 2022
# This program uses a list as a parameter


import random

import constants


def average_of_numbers(list_of_numbers):
    # this functions add up all the numbers in the list

    median = 0

    for counter in range(0, len(list_of_numbers)):
        median += list_of_numbers[counter]

    median = median / constants.MAX_ARRAY_SIZE
    return median


def main():
    # this function uses a list

    random_numbers = []
    average = 0

    # input
    print("The numbers are ")
    for loop_counter in range(constants.MAX_ARRAY_SIZE):
        a_single_number = random.randint(0, 100)
        random_numbers.append(a_single_number)
        if a_single_number < 10:
            print("{}  added at position {}".format(a_single_number, loop_counter))
        else:
            print("{} added at position {}".format(a_single_number, loop_counter))

    average = average_of_numbers(random_numbers)

    print("\nThe average of all the numbers is: {0} ".format(average))


if __name__ == "__main__":
    main()
