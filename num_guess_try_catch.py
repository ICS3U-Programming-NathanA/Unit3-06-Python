#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 17 2022
# This program asks the user for a number between 0 and 9 and then sees if they got the same number as the computer

import random


def main():
    # generates a number between 0 and 9
    random_num = random.randint(0, 9)

    # Get the the number they guessed
    user_num = input("Enter a number between 0 and 9: ")

    # An If statement to see if they got the same number as the generated number then display the results
    if random_num == user_num:
        print("You guessed the correct number")
    else:
        print("You guessed the incorrect number")

    try:
        user_num_as_a_number = int(user_num)
        print("")
    except ValueError:
        print("This number is not a integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
