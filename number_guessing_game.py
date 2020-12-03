#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program is number guessing game

import random


def main():
    # this function checks if number is not 5

    # input
    your_number = int(input("Enter your number "))
    print("")

    # process
    random_number = random.randint(1, 9)  # a number between 1 and 9

    if random_number == your_number:
        # output
        print("You are right!")
        print("random number is {}".format(random_number))
    else:
        print("you are wrong")
        print("random number is {}".format(random_number))


if __name__ == "__main__":
    main()
