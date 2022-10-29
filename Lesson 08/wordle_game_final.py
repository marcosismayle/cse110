"""
Program: 07 Prove: Assignment Milestone - Wordle Game
Author: Brother Burton

Purpose: Word guessing game
"""
print('Welcome to the word guessing game!')
secret_word = 'mosiah'
spaces = '_ '* len(secret_word)
print()
print(f'Your hint is: {spaces}')

guess = input('What is your guess? ')
guess_count = 0


while guess.lower() != 'mosiah':
    print('Your guess was not correct.')
    print()
    print(f'Your hint is: {spaces}')
    guess = input('What is your guess? ')
    guess_count += + 1



print('Congratulations! You guessed it!')
print(f'It took you {guess_count} guesses.')