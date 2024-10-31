import random

def guess(x):
    random_number = random.randint(1, 10)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number btween 1 and {x}: '))
        print(guess)
        if guess < random_number: 
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too hight.')
        
    print(f'Yay, congrats. You have guessed the number {random_number} correctly .')

guess(10)
        