#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Dec 15th, 2022
# This program generates 10
# random numbers, between 1 and 100, and
# calculates the average out of all those numbers.

import random
import constants


def main():
    # Empty list where you can
    # store the 10 random numbers
    random_numbers = []
    sum = 0

    # Use for loop to generate the 10 random numbers
    for counter in range(constants.MAX_ARRAY_SIZE):

        # Random number generator
        random_int = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Adds random number to list
        random_numbers.append(random_int)

        print(f"Added {random_int} to list at index {counter}")

        # Adds the value of the number to sum
        sum += random_int

        # Divides the sum by the amount of
        # numbers generated which is 10
        average = sum / constants.MAX_ARRAY_SIZE

    # Display the average to the user
    print(f"The average of the 10 numbers generated is: {average}")



if __name__ == "__main__":
    main()
