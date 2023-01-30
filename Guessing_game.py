import random

def guess(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < rand_num:
            print(f'Sorry try again, num too low')
        elif guess > rand_num:
            print(f'Sorry try again, num too high ')
    print(f'Congrats you have guessed the number {rand_num}')
def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high H, too low L or correct C : ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("the computer guess your num correctly " + " guess ") 
comp_guess(10)   


    