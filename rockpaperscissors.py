# rockpaperscissors.py
import random
choice_list = ['rock', 'paper','scissors']
user_input = input("rock, paper, or scissors?: ")
computer_choice = random.choice(choice_list)
print(f"Your opponent chose {computer_choice}")
if user_input == 'rock':
    if computer_choice == 'rock':
        print('Tie!')
    if computer_choice == 'scissors':
        print('You win!')
    if computer_choice == 'paper':
        print('You lose!')
if user_input == 'paper':
    if computer_choice == 'paper':
        print('Tie!')
    if computer_choice == 'rock':
        print('You win!')
    if computer_choice == 'scissors':
        print('You lose!')
if user_input == 'scissors':
    if computer_choice == 'scissors':
        print('Tie!')
    if computer_choice == 'paper':
        print('You win!')
    if computer_choice == 'rock':
        print('You lose!')
response = input('Do you want to play again? Yes or no? ')
if response == 'no':
        print('Okay! Have a great day!')
while response == 'Yes' or 'yes':
    user_input = input("rock, paper, or scissors?: ")
    computer_choice = random.choice(choice_list)
    print(f"Your opponent chose {computer_choice}")
    if user_input == 'rock':
        if computer_choice == 'rock':
            print('Tie!')
        if computer_choice == 'scissors':
            print('You win!')
        if computer_choice == 'paper':
            print('You lose!')
    if user_input == 'paper':
        if computer_choice == 'paper':
            print('Tie!')
        if computer_choice == 'rock':
            print('You win!')
        if computer_choice == 'scissors':
            print('You lose!')
    if user_input == 'scissors':
        if computer_choice == 'scissors':
            print('Tie!')
        if computer_choice == 'paper':
            print('You win!')
        if computer_choice == 'rock':
            print('You lose!')
    response = input('Do you want to play again? Yes or no? ')
    if response == 'no':
        print('Okay! Have a great day!')
