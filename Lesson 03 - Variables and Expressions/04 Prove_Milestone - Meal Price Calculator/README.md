# 03 Prove: Milestone - Meal Price Calculator

**Regarding Milestones and Assignments:** For the prove assignments for Lessons 03 and 04, you'll be working on the same program. For this lesson's assignment (03 Prove: Milestone) you will complete part of the overall program. Then, you'll finish the program in the next lesson.

Read over the full requirements first, then at the bottom of this page, you'll see which features are required for the milestone at the end of Lesson 03.

## Overview

Programs can obtain information from users and then combine those values to compute meaningful results. In this assignment, you will write a program to calculate the price of a meal.

## Instructions

Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.

Keep in mind that some of these values are floating point numbers (they can have decimals) and some of them are integers (whole numbers).

Ask the user for the following:

- The price of a child's meal (floating point)

- The price of an adult's meal (floating point)

- The number of children (integer)

- The number of adults (integer)

- The sales tax rate (floating point)

Then, complete the following steps:

- Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal, and multiplying the number of adults by the price of their meal and adding those two values together.

- Display the subtotal.

>***Hint from Instructor:***
As you will see in the requirements list below, this is as far as you need to get for the milestone requirements of Lesson 03, but you should try to get as far as you can during Lesson 03 to make it even easier for yourself in the next lesson, especially if you run into trouble.

- Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.

- Compute and display the total price of the meal by adding the subtotal and the sales tax.

Finally:

- Ask the user for the the payment amount (floating point)

- Compute and display the change.

A sample run of the program might look as follows:

    What is the price of a child's meal? 4.50
    What is the price of an adult's meal? 9.00
    How many children are there? 4
    How many adults are there? 2
    What is the sales tax rate? 6

    Subtotal: $36.00
    Sales Tax: $2.16
    Total: $38.16

    What is the payment amount? 40
    Change: $1.84

Another example, in which the user typed different values, might look like this:

    What is the price of a child's meal? 2.25
    What is the price of an adult's meal? 6.99
    How many children are there? 2
    How many adults are there? 1
    What is the sales tax rate? 4

    Subtotal: $11.49
    Sales Tax: $0.46
    Total: $11.95

    What is the payment amount? 20
    Change: $8.05

## Showing Creativity and Exceeding Requirements

For this assignment, you could add anything else to the meal, such as drinks, appetizers, or a tip percentage, or anything else you can think of. Play around with different ideas and see what you can learn!

## Milestone Requirements

At the end of Lesson 03, to help make sure you are on track to finish the assignment, you need to complete the following:

1. Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.

2. Ask the user for the number of adults and children and store these values properly into variables as integers.

3. Ask the user for the sales tax rate and store the value properly as a floating point number.

4. Compute and display the subtotal (don't worry about rounding to two decimals at this point).

## Final requirements

At the end of Lesson 04, in addition to the milestone requirements above, you need to also complete the following:

1. Compute and display the sales tax.

2. Compute and display the total.

3. Ask the user for the payment amount and store the value properly as a floating point number.

4. Compute and display the change.

5. Include a dollar sign ($) before each displayed value.

6. Display each value to two decimals.

7. Double check that the calculations are correct.

8. Show creativity and exceed the core requirements by adding additional features.

9. Use good style in your program, including variable names and whitespace.

## Submission

For the milestone submission, complete the associated I-Learn quiz that asks you to declare which of the milestone steps you successfully finished. Then, upload your code to I-Learn as well.

Please be aware that the instructor will not be providing detailed feedback on the code submission for milestones. This is a chance for you to check in and show progress. Then, you'll receive detailed feedback on your final submission.

In the next lesson, you'll finish the remaining requirements.
