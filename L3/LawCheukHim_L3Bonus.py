#edit word here
target='hangman'
#edit number of chances here
chance=10
state=[]
for i in range(0,len(target)):
    state.append(0)
wrong=[]
while True:
    for i in range(0,len(target)):
        if state[i]==0:
            print('_', end=' ')
        else:
            print(target[i], end=' ')
    print()
    print(wrong)
    if 0 in state:
        state=state
    else:
        break
    if len(wrong)<chance:
        print('You have %d chances left.'%(chance-len(wrong)))
    else:
        break
    guess=input('Guess a letter (lowercase) : ')
    if guess in target:
        for i in range(0,len(target)):
            if target[i]==guess and state[i]==0:
                state[i]=state[i]+1
    elif guess in wrong:
        guess=guess
    else:
        wrong.append(guess)
if 0 in state:
    print('Sorry!  You\'ve run out of chance.  The correct word is %s.'%target)
else:
    print('Congratulations!  You\'ve got the correct word - %s.'%target)
input()
