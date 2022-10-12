# 05 Prepare: Checkpoint

Practicing If Statements

## Overview

Practice the mechanics of **if** statements.

## Assignment

I. COMPARING NUMBERS

Write a program that asks the user for two integers.

Then, write three separate **if/else** statements as follows:

- If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

- If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

- If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

II. COMPARING STRINGS

Have the program ask the user for their favorite animal. Then write an **if** statement as follows:

- Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

> Hint from Instructor:
> When you write the program, you'll "hard code" your favorite animal into the program as the string to check against.
>
> Hard coding just means that you write it directly into the program, sometimes called a **literal** value. Because this value doesn't come from a user or a file or anything, it will always be used, every time the program is run.

Here is an example of the program when it runs:

    What is the first number? 4
    What is the second number? 3
    The first number is greater
    The numbers are not equal
    The second number is not greater

    What is your favorite animal? giraffe
    That one is not my favorite.

Another example:

    What is the first number? 1009
    What is the second number? 5250
    The first number is not greater
    The numbers are not equal
    The second number is greater

    What is your favorite animal? bear
    That's my favorite animal too!

And finally, note that in this example, the animal matches, even though the case is different:

    What is the first number? 42
    What is the second number? 42
    The first number is not greater
    The numbers are equal
    The second number is not greater

    What is your favorite animal? BEAR
    That's my favorite animal too!

## Sample Solution

When your program is finished, please view a sample solution of this program to compare your approach to that one.

You should work to complete this checkpoint program first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

- Sample solution: check05_sample.py

## Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

01. Test the first part of your program with pairs of numbers where the first is greater and also where the second is greater. Verify that all three values that are printed are correct.

02. Test it with two numbers that are equal. Verify that all three values that are printed are correct.

03. Test the second part of your program with an animal that is different. Verify that the correct message is shown.

04. Test it with an animal that is the same. Verify that the correct message is shown.

05. Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.

## Submission

When complete, please report your progress in the associated I-Learn quiz.
