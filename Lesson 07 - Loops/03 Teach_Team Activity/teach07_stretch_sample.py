
"""
File: teach07_stretch_sample.py
Author: Brother Burton

Purpose: Guess my number game, including the stretch challenges.
"""

import random

keep_playing = "yes"

# As long as they say "yes" we will keep playing
while keep_playing == "yes":
    magic_number = random.randint(1, 100)

    # this variable will keep track of how many guesses it took
    guess_count = 0

    guess = -1

    # Keep going as long as the guess doesn't match the magic number
    while guess != magic_number:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1

        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print("You guessed it!")

    # At this point, they have guessed it correctly
    print(f"It took you {guess_count} guesses")

    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thank you for playing. Goodbye.")