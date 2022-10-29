import random

input('Press enter to start!')

play_again = 'Y'

while play_again.lower() not in ('y', 'n'):
    print('Invalid option! Try again.')
    play_again = input('Do you want to play again? Y/N ')

    if play_again.lower() == 'y':
        input('Lets play')
        play_again = input('Do you want to play again? Y/N ')
    else:
        print('Ok! Bye.')





'''
play_again = 'Y'

while play_again.lower() != ('y', 'n'):
    print('Invalid option! Try again.')
    play_again = input('Do you want to play again? Y/N ')
else:
    if play_again.lower() == 'y':
        number = random.randint(1, 100)

        counting = 0

        guess = 0

        while guess != number:
            guess = int(input('What is your guess? '))
            counting += 1
                
            if guess < number:
                print('Higher')
            elif guess > number:
                print('Lower')
            else:
                    print('You guessed it!')

        print(f'Number of gesses is: {counting}')

        play_again = input('Do you want to play again? Y/N ')

    print('Ok! Bye!')
    '''