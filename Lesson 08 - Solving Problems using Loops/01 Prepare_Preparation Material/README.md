# 08 Prepare: Preparation Material

## Overview

In this lesson, you will continue working with loops and learning how to solve more complex problems.

## Preparation Material

In the previous lesson, you learned about **while** loops. In this lesson, you will build on that foundation to learn about another kind of loop called a **for** loop.

Watch the following videos which discuss both kinds of loops:

- [Loops](https://www.youtube.com/watch?v=LrOAl8vUFHY&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=27) (5 mins)

- [Demo: Loops](https://www.youtube.com/watch?v=rAvD-6MpTw4&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=28) (3 mins)

As shown, there are a few different ways you can tell the computer to loop through code over and over again.

I. LOOPING THROUGH A LIST

One example of looping, is to loop, or iterate, through each item of a collection or a list, one at a time. You will learn about lists in more detail in future lessons, but the following shows an example of looping through a list of words to print them on the screen one at a time:

    items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

    for item in items:
        print(f"The item is: {item}")

The output of this code is:

    The item is: crayon
    The item is: scissors
    The item is: paper
    The item is: glitter glue
    The item is: markers
    The item is: pens    

Just as with **if** statements, the colon **:** at the end of your **for** statement tells the computer that there is a block of code coming. Then, you indent all the code that is in the block. The code that is indented is the code that will be run on each item.

When looping through each item, you can do much more with it than simply printing it out. You could include an **if** statement, to check if it meets certain conditions, and then use it in a math expression, or anything else that you've learned how to do in your programs.

>**Frequently Asked Questions**
>
>What about the variable **item**? Is that a special name? Where does it get defined?
>
>There is nothing special about the name **item** in this case. It could have just as easily been called **thing** or **writing_instrument**.
>
>The for loop syntax here is very clever. When you type **for item in items:**, the list variable, **items** must already exist, but the variable for each individual element of the list, in this case **item**, is defined right in that statement. In short, it's saying, "Go through each element of this list and assign a new variable **item** to be the value each time through.

II. LOOPING THROUGH NUMBERS

It's very common in programming to want to loop through a series of numbers. You could create a list of numbers, just like the list of words in the last example, like this:

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

But this could get really long if you wanted to work with a large amount of numbers, so there is an easier way, using **range**.

You can create the same list of numbers like this:

    numbers = range(10)

This creates a list of numbers for you that starts at **0** and goes up until (but not including) **10**.

You could assign this list to a variable like **numbers** as in the example above, and then loop through each number in the list of numbers, but it is more common to just put the **range** code right in your for loop like this:

    for number in range(10):
        print(number)

The output of this code is:

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

>**Hint from Instructor**
>
>In programming languages we usually start counting at 0 instead of 1. There are reasons for this, but more than anything, it's just something you'll have to get use to.

The **range** function gives you other options like starting at a different number, or counting by 3's, or even going backwards. In all of these cases, the idea of looping through the values is the same. You start with the first one and then continue on, one by one, through the list.

To start with a different number, you provide two values to the **range** function. If you provide two numbers, it will start with the first one and continue up until (but not including) the second one.

If you provide three values to the **range** function, it will use the third number as the "step size" or in other words the number to count by.

    # This loop will start with 100, and go up to, but not including 200
    for i in range(100, 200):
        print(i)

    # This loop will do the same thing, but this time, it will count by 10's
    for i in range(100, 200, 10):
        print(i)

III. LOOPS WITHIN LOOPS

A loop will blindly repeat any code that is in its body. That code could include if statement, mathematics, new variable definitions, or anything else—including other loops!

The following example displays the numbers 0-4:

    for i in range(5):
        print(i)

Output:

    0
    1
    2
    3
    4

We can add a second, inner loop, that for each one of those displays the numbers 10-12 (with two - characters in front to make it easier to visualize).

    for i in range(5):
        print(i)
        for j in range(10, 13):
            print(f"--{j}")

Output:

    0
    --10
    --11
    --12
    1
    --10
    --11
    --12
    2
    --10
    --11
    --12
    3
    --10
    --11
    --12
    4
    --10
    --11
    --12

Notice how the inner loop is run every time the outer loop displays it's number. Inner loops can be very helpful in iterating through a two-dimensional structure, such as the pixels in an image.

>**Hint from Instructor**
>
>While we generally prefer variable names that are more descriptive than a single letter, if the variable will only be used for counting in a simple loop it is considered standard to use i. Then, if you have an inner loop, you use j, and a third inner loop would be k. If you have more than three loops you should consider if there is a simpler way to accomplish your task, and if there really isn't, you should at least move to more descriptive variable names at that point.

IV. LOOPING THROUGH STRINGS

You can iterate through each letter of a string using either style of for-loop. For example, you can loop through each letter one at a time with the following code:

    first_name = "Brigham"
    for letter in first_name:
        print(f"The letter is: {letter}")

The output of this code is:

    The letter is: B
    The letter is: r
    The letter is: i
    The letter is: g
    The letter is: h
    The letter is: a
    The letter is: m

Just as before, there is nothing special about the variable name **letter**, any name could have been used, but the choice of **letter** helps us keep the code nice and easy to read.

## Accessing Letters by Position

Sometimes you need to access a letter by its position (or index) in a string. In other words, you might want to know the third or seventh letter in a string. This will be useful when comparing letters at the same place in two strings, such is in your project for this lesson.

You can access a specific letter in a string by using the square brackets **[]**, such as **word[3]** or **word[12]**. But be aware that that the count starts at 0, so you will use **3** to get the *fourth* letter (not the third letter). The following example gets the fourth letter of the name:

    first_name = "Brigham"

    fourth_letter = first_name[3] # Notice, using 3 instead of 4
    print(fourth_letter) # outputs a 'g' on the screen

## Iterating through each letter using an index

In the previous sections you learned how to iterate through each letter in a string, but this only gave you access to the letter but not the index of that letter. In many cases, this is sufficient. However, in other cases you need to know both the letter and its index. (For example, in your project you need to know the letter and also check its position in another word.)

In this case, rather than looping through letters, you can loop through the index numbers. If you knew the length of the word, you could do this as follows:

    word = "book"
    number_of_letters = 4

    for index in range(number_of_letters):
        print(index)

This code will output the following:

    0
    1
    2
    3

Then, you can use the square brackets to access the letter at that index as follows:

    word = "book"
    number_of_letters = 4

    for index in range(number_of_letters):
        letter = word[index]
        print(f"Index: {index} Letter: {letter}")

This code will output the following:

    Index: 0 Letter: b
    Index: 1 Letter: o
    Index: 2 Letter: o
    Index: 3 Letter: k

With this example, you have access to both the letter and the index at each step of the loop.

I. FINDING THE STRING LENGTH

The previous example assumed the number of letters, or *length* of the string, would always be 4, but this will not work if the string has more or fewer letters. Instead of typing the 4 directly, you can let the computer find the length by using the **len** function. The following code shows how to use **len** to get the length of a string:

    dog_name = input("What is your dog's name? ")
    letter_count = len(dog_name)

    print(f"Your dog's name has {letter_count} letters")

The output of this code could be:

    What is your dog's name? Rover
    Your dog's name has 5 letters

Combining the **len** function with the earlier loop is very powerful, because now you can iterate through the indexes and letters of strings of any length as follows:

    word = "book"
    number_of_letters = len(word) # Notice this can now work for any string

    for index in range(number_of_letters):
        letter = word[index]
        print(f"Index: {index} Letter: {letter}")

This code will output the following:

    Index: 0 Letter: b
    Index: 1 Letter: o
    Index: 2 Letter: o
    Index: 3 Letter: k

## Lists

Many of the examples you see with **for** loops often iterate through a list of items, including numbers in a list, or letters in a string. This naturally extends to working with other properties of lists, such as finding the length of the word or the position of the letter.

This lesson introduces some of these concepts, but please be aware that the next lesson focuses entirely on working with lists. So, while you'll start to use lists a little bit now, you will get much more practice and learn the details even better as you continue on to the next lesson.

## (Optional) Python Enumerate

Using a for loop and the length of the string is a standard way to access both the index and the letter. However, Python also has a way to access both of these variables directly using a special function called **enumerate** as shown in the following example:

    first_name = "Brigham"

    # Notice by using enumerate, we specify both i and letter
    for i, letter in enumerate(first_name):
        print(f"The letter {letter} is at position {i}")

The output of this code is:

    The letter B is at position 0
    The letter r is at position 1
    The letter i is at position 2
    The letter g is at position 3
    The letter h is at position 4
    The letter a is at position 5
    The letter m is at position 6

This is a little different than the standard **for** loop, because it returns two variables. This function is not supported in many languages, but it is available in Python and you are welcome to use it in your programs if you would like.
