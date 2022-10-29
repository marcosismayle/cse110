# 07 Teach: Team Activity

Guess My Number Game

## Overview

In the Guess My Number game the computer picks a magic number, and then the user tries to guess it. After each guess, the computer tells the user to guess "higher" or "lower" until they guess the magic number.

This assignment is a little tricky, because it brings together many of the concepts you've learned in this course including loops and if statements.

## Assignment

I. HAVING THE COMPUTER PICK A RANDOM NUMBER

There is a random number library included with Python that contains a number of different functions to generate random numbers, depending on if you want integers, floating point numbers, and from different statistical distributions.

The only function you will need from this library is called randint. To use it, you give it two numbers and it returns back a random number in that range. In order to use this function you need to import it from the random library.

The following code shows how to import the function and use it to get a random number from 1 to 10.

        import random

        number = random.randint(1, 10)
        print(number)

II. CORE REQUIREMENTS

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

1. >Start by asking the user for the magic number. (In future steps, we will change this to have the computer generate a random number, but to get started, we'll just let the user decide what it is.)
    >
    > Ask the user for a guess.
    >
    >Using an if statement, determine if the user needs to guess higher or lower next time, or tell them if they guessed it.
    >
    >At this point, you won't have any loops.

    The following shows the expected output at this point:

        What is the magic number? 6
        What is your guess? 4
        Higher

    --

        What is the magic number? 6 
        What is your guess? 7
        Lower

    --

        What is the magic number? 6
        What is your guess? 6
        You guessed it!

2. >Add a loop that keeps looping as long as the guess does not match the magic number.
    >
    >At this point, the user should be able to keep playing until they get the correct answer.

    The following shows the expected output at this point:

        What is the magic number? 18
        What is your guess? 5
        Higher
        What is your guess? 6
        Higher
        What is your guess? 7
        Higher
        What is your guess? 20
        Lower
        What is your guess? 19
        Lower
        What is your guess? 18
        You guessed it!

3. >Instead of having the user supply the magic number, import the random library and use it to generate a random number from 1 to 100.
    >
    >Play the game and make sure it works!

III. STRETCH CHALLENGE

1. >Keep track of how many guesses the user has made and inform them of it at the end of the game.

2. >After the game is over, ask the user if they want to play again. Then, loop back and play the whole game again and continue this loop as long as they keep saying **"yes"**.

## Sample Solution

When your program is finished, please view the sample solution for this program to compare it to your approach.

You should work to complete this team activity for the one hour period first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

- Sample solution (Core requirements): teach07_sample.py

- Sample solution (Stretch challenges): teach07_stretch_sample.py

## Submission

When complete, please report your progress in the associated I-Learn quiz.

If you decided to do additional work on the program after your team activity, either by yourself or with others, feel free to include that additional work when you report on your progress in I-Learn.
