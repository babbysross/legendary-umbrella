# guess the random number game

from random import randint


def rand():
    secretno = randint(1, 20)
    for guesses in range(1, 7):
        guess = int(input('Take a guess: '))
        if guess < secretno:
            print('Too low, try again!')
        elif guess > secretno:
            print('Too high, you\'ll get it next time!')
        else:
            break

    if guess == secretno:
        print('Good guess, you got it! You took ' +
            str(guesses) + ' tries to get it right.')
    else:
        print('Better luck next time, it was ' + str(secretno) + '!')

name = input('Hi! What\'s your name? \n')
print('Well, ' + name + ', I\'m thinking of a number between 1 and 20')
rand()