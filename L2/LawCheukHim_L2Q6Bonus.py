import random
print('''Welcome to the Banana Guessing Game!
Dave hid some bananas.  Your task is to find out the number of bananas he hid.''')
target=random.randint(1,100)
player=0
while True:
    if ( player%2==0 ):
        guess=int(input('Player 1, input your guess: '))
    else:
        guess=int(input('Player 2, input your guess: '))
    if ( guess==target ):
        break
    elif (guess<1 or guess>100):
        print('Guess out of range.  Try again!')
        continue
    elif (guess<target):
        print('Guess too small.')
    elif (guess>target):
        print('Guess too large.')
    player=player+1
if ( player%2==0 ):
    print('Congratulations!  Player 1 wins.')
else:
    print('Congratulations!  Player 2 wins.')
input()
