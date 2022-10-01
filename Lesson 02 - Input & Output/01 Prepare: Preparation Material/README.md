# 02 Prepare: Preparation Material

## **Overwiew**

In this lesson, you will build on the basic input/output ideas from your programs in the last lesson, and learn to store more information and display it using better formatting. While not all programs use the console input and output approach that we have taken thus far (where people type the answers and see the results in text), almost all programs make use of many string variables and combine and format them in one form or another.

## **Preparation Material**

I. VARIABLES

A variable is a place on the computer memory to store a data.

A variable must have a clear name.

II. COMMENTS

Comments are a way for programers to include notes in the code. They don't affect the program in any way, but help others programmers understand the code. To add a comment in Python, include the # sign before the text.

***Videos:***

- [COMMENTS](https://www.youtube.com/watch?v=kEuVvUc1Zec&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=8)
- [DEMO: COMMENTS](https://www.youtube.com/watch?v=fbek7n6ecWM&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=8)

III. COMBINING AND FORMATING STRINGS

Strings are variables that are a sequence of characters (for example, letters).

- [STRING CONCEPTS](https://www.youtube.com/watch?v=tSebLz1hNpA&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=10)
- [DEMO: STRINGS](https://www.youtube.com/watch?v=zv3cVJHCqXA&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=11)

*Example 01:*

    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')

    print('Hello, ' + first_name.capitalize() + '' + last_name.capitalize())

- [FORMATING STRINGS](https://www.youtube.com/watch?v=bQQqxysLIGE&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=11)
- [DEMO: FORMATING STRINGS](https://www.youtube.com/watch?v=E850-MF22P0&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=12)

*Example 02:*

    first_name = 'Marcos'
    last_name = 'Ribeiro'

    output = 'Hello, ' + first_name + ' ' + last_name
    print(output)

*Example 03:*

    first_name = 'Marcos'
    last_name = 'Ribeiro'

    output = 'Hello, {} {}' .format(first_name, last_name)
    print(output)

*Example 04:*

    first_name = 'Marcos'
    last_name = 'Ribeiro'

    output = 'Hello, {0} {1}' .format(first_name, last_name)
    print(output)

*Example 05:*

    first_name = 'Marcos'
    last_name = 'Ribeiro'

    output = f'Hello, {first_name} {last_name}'
    print(output)

Some formating functions:

|            Code               |       Result        |
|-------------------------------|---------------------|
| words = "the cat IN THE hat"  | the cat IN THE hat  |
| words.capitalize()            | The cat in the hat  |
| words.title()                 | The Cat In The Hat  |
| words.upper()                 | THE CAT IN THE HAT  |
| words.lower()                 | the cat in the hat  |
| words.count("t")              | 3                   |
| words.lower().count("t")      | 4                   |
