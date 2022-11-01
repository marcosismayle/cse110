"""
File: favorite_letter.py
Author: Marcos Ismayle
Purpose: Write a program that asks the user for their favorite letter. Then, loop through a programmed word one letter at a time. If the letter in the programmed word is the user's favorite, print it out as a capital letter (or "hide" it), if not, print it out as a lower case letter.
"""

'''
1. Create a string variable to hold the word "Commitment".

Write code that loops through the word letter by letter. If the letter is "m", print it as a capital letter. If the letter is anything else, print it out as a lowercase letter.

For this part, it is ok to print each letter on it's own line.'''


# word = 'Commitment'

# for letter in word:
    
#     if letter == 'm':
#         print(letter.upper(), end='')
#     else:
#         print(letter.lower(),end='')

'''
2. Change the print statements so that each letter is not printed on its own line, but rather they are printed out next to each other on the same line.

Also, change the program to allow the user to specify the letter (rather than always using "m"). Make sure your program matches the letter in the word, regardless of whether the user entered it as a capital or lowercase, and regardless of whether that letter was a capital or lowercase in the original word.'''


# favorite_letter = input('What is your favorite letter? ')
# word = 'Commitment'

# for letter in word:
    
#     if letter == favorite_letter:
#         print(letter.upper(), end='')
#     else:
#         print(letter.lower(),end='')

'''
3. Change the program, so that instead of capitalizing the user's favorite letter, it "hides" it, and replaces it with an underscore in the display.'''

favorite_letter = input('What is your favorite letter? ')
word = 'Commitment'

for letter in word:
    
    if letter == favorite_letter:
        print('_', end='')
    else:
        print(letter.lower(),end='')