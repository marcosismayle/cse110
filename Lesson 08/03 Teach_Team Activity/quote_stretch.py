"""
File: quote_stretch.py
Author: Marcos Ismayle
Purpose: Write a program that asks the user for their favorite letter. Then, loop through a programmed word one letter at a time. If the letter in the programmed word is the user's favorite, print it out as a capital letter (or "hide" it), if not, print it out as a lower case letter.
"""

quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'

repeat = 'yes'

while repeat == 'yes':
    number = int(input('Please enter a number: '))

    for i, letter in enumerate(quote):
        
        if i % number == 0:
            print(letter.upper(), end='')
        else:
            print(letter.lower(),end='')
    
    print()
    repeat = input('Would you like to enter another number? ')
print('Goodbye')