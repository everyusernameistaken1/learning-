#Guess a number
import random
secretNumber=random.randint(1,10)

#Ask for name
print('Hello! What is your name?')
name= input()

print('Well, ' + name + ' I am thinking of a number between 1 and 10.')

print('DEBUG: Secret number is ' +str(secretNumber))

for guessesTaken in range(1,7):
    print('Take a guess!')
    guess= int(input())

    if guess < secretNumber:
            print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #This condition is for the correct guess.

if guess == secretNumber:
    print('You guessed right! You took ' + str(guessesTaken) + ' guesses.')


else:
    print('The correct number was ' + str(secretNumber))
