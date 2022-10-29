"""
Program: 07 Prove: Assignment Milestone - Wordle Game
Author: Marcos Ismayle

Purpose: Word guessing game
"""

print('Welcome to the word guessing game!')
print()

secret_word = 'mosiah'
guess = input('What is your guess? ')
guess_count = 0

while guess.lower() != 'mosiah':
    print('Your guess was not correct.')
    print()
    guess = input('What is your guess? ')
    guess_count += + 1
    
print('Congratulations! You guessed it!')
print(f'It took you {guess_count} guesses.')