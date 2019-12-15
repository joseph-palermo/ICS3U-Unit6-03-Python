#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: December 2019
# This program finds the smallest random number


import random


def calculate(number_list):
    # this function finds the smallest number

    # variables
    small_number = 100

    # process
    for counter in number_list:
        if counter < small_number:
            small_number = counter

    # output
    return small_number


def main():
    # this function generates 10 random numbers then outputs the smallest

    rand_number = []

    # process
    for counter in range(10):
        random_number = random.randint(1, 100)
        print(random_number)
        rand_number.append(random_number)

    # calling a function
    smallest_number = calculate(rand_number)

    # output
    print("")
    print("The smallest number is", smallest_number)


if __name__ == "__main__":
    main()
