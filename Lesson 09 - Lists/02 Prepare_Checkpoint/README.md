# 09 Prepare: Checkpoint

## Overview

Practice working with lists.

## Assignment

Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

Hint 1: You should keep asking for friends, as long as the name is not "end". (Does this sound like a loop you know?)

Hint 2: Be careful not to add "end" to the list of names when it is typed. You can check if the name is or is not something before you add it to the list.

The following examples show the expected output:

    Type the name of a friend: Matthew
    Type the name of a friend: Mark
    Type the name of a friend: Luke
    Type the name of a friend: John
    Type the name of a friend: end

    Your friends are:
    Matthew
    Mark
    Luke
    John

Another example could be the following:

    Type the name of a friend: Peter
    Type the name of a friend: James
    Type the name of a friend: John
    Type the name of a friend: end

    Your friends are:
    Peter
    James
    John

## Sample Solution

When your program is finished, please view a sample solution of this program to compare your approach to that one.

You should work to complete this checkpoint program first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

- Sample solution: check09_sample.py

## Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

1. Test it with just one name.

2. Test it with 3–4 names

3. Make sure that the word "end" doesn't display at the end of your list of friends.

4. Test it by entering the same name 3 times before typing end (the result should be that you see the name repeated 3 times in the list).

5. Test it with no names, just the word end, and make sure it doesn't cause any errors.

## Submission

When complete, please report your progress in the associated I-Learn quiz.
