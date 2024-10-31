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

def computer_guess(x):
    low = 1
    hight = x 
    feedback = ''
    while feedback != 'c':
        if low != hight:
            guess = random.randint(low, hight)
        else:
            guess = low 
        feedback = input(f'Is {guess} too hight (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            hight = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(100)
        