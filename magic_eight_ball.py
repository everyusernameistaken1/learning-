#magic eight ball
import random
print('Welcome!')
input('Ask a question...')
prophecy_list=['yes','never','it is certain','if your heart desires']
print(f'{random.choice(prophecy_list)}')
response = input("Do you want to ask another question? Yes or no?")
while response == 'yes':
    input('Ask a question...')
    prophecy_list=['yes','never',' it is certain','if your heart desires']
    print(f'{random.choice(prophecy_list)}')
    response = input("Do you want to ask another question? Yes or no?")
    if response == 'no':
        print('Are you scared?')
