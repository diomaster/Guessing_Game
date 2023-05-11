import random

num = random.randint(1, 100)

name = input("Hello! Tell me your name! ")
guesses = 0
print('okay! ' + name + ' I am thinking of a number between 1 and 100 what is it?: ')


while guesses < 10:
    guess = int(input())
    guesses += 1
    if guess < num:
        print('nope too low')
    if guess > num:
        print('no no no too high!')
    if guess == num:
        break
if guess == num:
        print('You did it you guess the number in ' + str(guesses) + ' tries!')
else:
        print('welp there was an attempt, the number was ' + str(num))