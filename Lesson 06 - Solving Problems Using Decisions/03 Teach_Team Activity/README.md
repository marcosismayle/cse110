# 06 Teach: Team Activity

Amusement Park Rides

## Overview

For this assignment, you'll work as a team to write a program for a fictitious amusement park ride.

I. THE SCENARIO: RIDER REQUIREMENTS

The local amusement park has just installed a new ride. Because of its speed and extreme twists and turns, it has very strict requirements for the riders, especially as it pertains to children or other shorter riders.

To help the ride attendants follow the rules, you've been asked to write an app to help them know if the riders are acceptable for the car.

The basic rules are as follows:

1. No one under 36 inches may ever ride, either by themselves or with another rider.

2. Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

3. If there are two riders and one of them is at least 18 years old, they may ride together.

## Assignment

Implement the ride requirements defined above. Your program should prompt for the riders' ages and heights, and then display a message indicating whether they can ride or not.

I. CORE REQUIREMENTS

1. Prompt the user for the age and height of the first person. Then, ask whether there is a second rider, and if so, ask for their age and height.

2. Handle the case of a single rider.

3. Finish implementing the basic rules.

An example run of the program may look as follows:

    What is the age of the first rider? 12
    What is the height of the first rider? 46
    Is there a second rider (yes/no)? no
    Sorry, you may not ride.

Another example may look as follows:

    What is the age of the first rider? 82
    What is the height of the first rider? 75
    Is there a second rider (yes/no)? yes
    What is the age of the second rider? 14
    What is the height of the second rider? 35
    Sorry, you may not ride.

And a final example:

    What is the age of the first rider? 82
    What is the height of the first rider? 75
    Is there a second rider (yes/no)? yes
    What is the age of the second rider? 14
    What is the height of the second rider? 36
    Welcome to the ride. Please be safe and have fun!

II. STRETCH CHALLENGE

In addition to the basic rules, the amusement park has added the following. Please implement each one for the stretch challenges:

1. If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.

2. If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)

3. If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

Whew! That's complicated! Now you see why they need an app.

## Sample Solution

When your program is finished, please view the sample solution for this program to compare it to your approach.

You should work to complete this team activity for the one hour period first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

- Sample solution (Core requirements): teach06_sample.py

- Sample solution (Stretch challenges): teach06_stretch_sample.py

## Submission

When complete, please report your progress in the associated I-Learn quiz.

If you decided to do additional work on the program after your team activity, either by yourself or with others, feel free to include that additional work when you report on your progress in I-Learn.
