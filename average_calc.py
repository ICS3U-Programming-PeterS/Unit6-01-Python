#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Dec 16, 2022
# This program uses a list as a parameter


import random

import constants


def sum_of_numbers(list_of_numbers):
    # this functions add up all the numbers in the list

    total = 0

    for counter in range(0, len(list_of_numbers)):
        total += list_of_numbers[counter]

    return total


def main():
    # this function uses a list

    random_numbers = []
    sum = 0

    # input
    print("The numbers are ")
    for loop_counter in range(constants.MAX_ARRAY_SIZE):
        a_single_number = random.randint(0, 100)
        random_numbers.append(a_single_number)
        print("{} added at position {}".format(a_single_number, loop_counter))

    sum = sum_of_numbers(random_numbers)

    print("\nThe sum of all the numbers is: {0} ".format(sum))


if __name__ == "__main__":
    main()
