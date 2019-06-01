print('How many dogs do you have?')
numdogs=input()
try:
    if int(numdogs) >= 3:
        print("That's a lot of dogs!")
    if int(numdogs)in range(0,3):
        print('Maybe a few more puppies!')
    if int(numdogs)<0:
        print('You can not have negative dogs!')
except ValueError:
    print('You did not enter a number.')
while numdogs != int:
    print('How many dogs do you have?')
    if int(numdogs) >= 3:
         print("That's a lot of dogs!")
    if int(numdogs)in range(0,3):
         print('Maybe a few more puppies!')
    if int(numdogs)<0:
          print('You can not have negative dogs!')
    
        
