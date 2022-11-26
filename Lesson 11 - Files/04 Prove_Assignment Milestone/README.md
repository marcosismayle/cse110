# 11 Prove: Assignment Milestone

Regarding Milestones and Assignments: Just as with the previous lessons, the Prove assignments for Lessons 11 and 12 will be working toward completing the same assignment. At the end of Lesson 11, you will complete part of the overall program, and then finish it in Lesson 12.

Read over the full requirements first. Then, at the bottom of this page, you'll see which features are required for the milestone at the end of Lesson 11.

## Overview

At this point in the course, you have learned how to use the major building blocks of programming, including variables, if-statements, loops, lists, and now files. Equipped with these tools, you can use them to solve real-world problems.

For this assignment you will write a program to analyze a dataset containing information about life expectancies over the years throughout the countries of the world.

## Project Description

The dataset you will be using comes from [OurWorldInData.org](https://ourworldindata.org/spanish-flu-largest-influenza-pandemic-in-history) from an article on the Spanish Flu. The first graph on that page shows the life expectancies over the years for various countries. If you click the "data" tab at the bottom of the graphic, you can download the source data.

You can also download the dataset directly here: [life-expectancy.csv](https://byui-cse.github.io/cse110-course/lesson11/life-expectancy.csv). This is a .csv (Comma Separated Values) file that contains the data you'll need with each column separated by commas. There are roughly 19,000 rows in this dataset.

This dataset is licensed under the [Creative Commons BY license](https://creativecommons.org/licenses/by/4.0/), you may also read the [Life Expectancy Data License](https://byui-cse.github.io/cse110-course/lesson11/life_expectancy_license.html).

Your task is to write a program to help analyze this large amount of data.

## Assignment

Download the dataset and write a Python program to analyze it to answer the following questions:

1. What is the year and country that has the lowest life expectancy in the dataset?

2. What is the year and country that has the highest life expectancy in the dataset?

3. Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.

A sample run could look as follows:

    Enter the year of interest: 1959

    The overall max life expectancy is: 86.751 from Monaco in 2019
    The overall min life expectancy is: 17.76 from Iceland in 1882

    For the year 1959:
    The average life expectancy across all countries was 54.95
    The max life expectancy was in Norway with 73.49
    The min life expectancy was in Mali with 28.077

## Milestone Requirements

At the end of Lesson 11, to help make sure you are on track to finish the assignment, you need to complete the following:

1. Download the dataset

2. Load the dataset in your Python program

3. Iterate through the data line by line

4. Split each line into parts

5. Find the lowest value for life expectancy and the highest value for life expectancy in the dataset. (Note that at this point, you just need the value for this, not the year and the country for that value.)

## Final Requirements

Finish the program by getting the answers to the questions above and adding the required functionality.

## Showing Creativity and Exceeding Requirements

You can show creativity and exceed the core requirements by adding any kind of data exploration or additional features. For example, you could:

- Identify the year and country that has the largest drop from one year to the next.

- Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.

- Look for interesting anomalies or patterns in the data.

- Find another dataset and work with it.

- Anything else you can think of!

## Submission

For the milestone submission, complete the associated I-Learn quiz that asks you to declare which of the milestone steps you successfully finished. Then, upload your code to I-Learn as well.

Please be aware that the instructor will not be providing detailed feedback on the code submission for milestones. This is a chance for you to check in and show progress. Then, you'll receive detailed feedback on your final submission.

When the final project is complete, upload your code along with your answers to the questions to I-Learn.
