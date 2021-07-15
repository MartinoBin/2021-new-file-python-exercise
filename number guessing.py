# use random module
import random

# Setting a random number
secretNumber =random.randint(1,10)
print('I am thinking a number from 1 to 100.')

# Setting a guess number.

for guesstaken in range (1,8):# Guesstaken for 7 times.
    
    print('\nTake a number:')
    guess=int(input())

    if guess < secretNumber:
        print('This number is too low, you have '+str(7-int(guesstaken))+' times left.')
    elif guess > secretNumber:
        print('This number is too high, you have '+str(7-int(guesstaken))+' times left.')
    else:
        break

if guess == secretNumber:
    print('\nYes, you got the right number ' + str(secretNumber) + ' in ' + str(guesstaken) +' times.')

else:
    print('\nYou run out of times. The number is '+ str(secretNumber))


