"""
Program: 07 Prove: Assignment Milestone - Wordle Game
Author: Brother Burton

Purpose: Word guessing game
"""
import os
import random

os.system('cls')
word_list = ['world', 'house', 'place', 'group', 'party', 'money', 'point', 'smith', 'night', 'water', 'nephi', 'order', 'power', 'court', 'level', 'child', 'south', 'bible', 'woman', 'north', 'sense', 'faith', 'table']
for word in word_list:
    secret_word = random.choice(word_list)
    hint = ' _ ' * len(secret_word)

print('Welcome to the word guessing game!')
print()
print(f'Your hint is: {hint}')

guess = input('What is your guess? ')
guess_count = 0
guessed_correctly = False

def process_guess(secret_word, guess):
    position = 0
    hint = ''
    for letter in guess:
        if letter == secret_word[position]:
            hint += f' {letter.upper()}'
        elif letter in secret_word:
            hint += f' {letter.lower()} '
        else:
            hint += ' _ '
        position += 1
    print(f'Your hint is: {hint}')
    return hint

while guess.lower() != secret_word:

    if len(guess) != len(secret_word):
        os.system('cls')
        print('Welcome to the word guessing game!')
        print()
        print('Sorry, the guess must have the same number of letters as the secret word.')
        print('Press enter to continue.')
        input()
        os.system('cls')
        print('Welcome to the word guessing game!')
        print()
        print(f'Your hint is: {hint}')
        guess = input('What is your guess? ')
        guess_count += 1
    else:
        os.system('cls')
        print('Welcome to the word guessing game!')
        print()
        guessed_correctly = process_guess(secret_word, guess)
        guess = input('What is your guess? ')
        guess_count += 1

os.system('cls')
print('Welcome to the word guessing game!')
print()    
print('Congratulations! You guessed it!')
print(f'It took you {guess_count} guesses.')
print()
