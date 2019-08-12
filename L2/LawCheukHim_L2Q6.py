import random
print('''Welcome to the Banana Guessing Game!
Dave hid some bananas.  Your task is to find out the number of bananas he hid.''')
target=random.randint(1,100)
print('Shhh, Dave hides %s bananas'%target)
count=0
while count<3:
    guess=int(input('Guess an integer in [1,100]\n'))
    if ( guess==target ):
        print('You got the correct guess in %d trial(s).'%(count+1))
        print('Dave\'s bananas are now all yours!')
        break
    elif (guess<1 or guess>100):
        print('Guess out of range.  Try again!')
        continue
    elif (guess<target):
        print('Guess too small.  %d chance(s) left.'%(2-count))
    elif (guess>target):
        print('Guess too large.  %d chance(s) left.'%(2-count))
    count=count+1
input()
