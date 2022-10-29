
"""
File: teach07_sample.py
Author: Brother Burton

Purpose: Guess my number game.
"""

import random

magic_number = random.randint(1, 100)

# I need to start the variable "guess" at something, but I don't want to start it as
# valid number that the computer may have chosen, so I'll start with -1
guess = -1

# Keep going as long as the guess doesn't match the magic number
while guess != magic_number:
    guess = int(input("What is your guess? "))

    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("You guessed it!")

