import random

'''1. Start by asking the user for the magic number. (In future steps, we will change this to have the computer generate a random number, but to get started, we'll just let the user decide what it is.)

Ask the user for a guess.

Using an if statement, determine if the user needs to guess higher or lower next time, or tell them if they guessed it.

At this point, you won't have any loops.

number = int(input('What is the magic number? '))
guess = int(input('What is your guess? '))

if guess < number:
    print('Higher')
elif guess > number:
    print('Lower')
elif guess == number:
    print('You guessed it!')'''

'''2. Add a loop that keeps looping as long as the guess does not match the magic number.

At this point, the user should be able to keep playing until they get the correct answer.

number = int(input('What is the magic number? '))
guess = int(input('What is your guess? '))

while guess < number:
    print('Higher')
    guess = int(input('What is your guess? '))

while guess > number:
    print('Lower')
    guess = int(input('What is your guess? '))
    
if guess == number:
    print('You guessed it!')'''

'''3. Instead of having the user supply the magic number, import the random library and use it to generate a random number from 1 to 100.

Play the game and make sure it works!'''

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input('What is your guess? '))

    if guess > number:
        print('Lower')
    elif guess < number:
        print('Higher')
    else:
        print('You guessed it!')