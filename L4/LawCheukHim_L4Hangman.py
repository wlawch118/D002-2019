#edit word here
secret='hangman'
#edit number of chances here
chance=10
opened=[]
wrong=[]

def printer(secret,opened):
    for i in range(0,len(secret)):
        if i in opened:
            print(secret[i], end=' ')
        else:
            print('_', end=' ')
    print()
def checker(secret,guess):
    if guess in secret:
        for i in range(0,len(secret)):
            if secret[i]==guess:
                opened.append(i)
    elif guess in wrong:
        guess=guess
    else:
        wrong.append(guess)
    return opened
    
print('Welcome to the HANGMAN game!')
while True:
    printer(secret,opened)
    print(wrong)
    win=True
    for i in range(0,len(secret)):
        if i in opened:
            opened=opened
        else:
            win=False
    if win==True:
        print('CONGRATULATIONS!  You\'ve got the correct word - %s.'%secret)
        break
    elif len(wrong)<chance:
        print('You have %d CHANCES left.'%(chance-len(wrong)))
    else:
        print('SORRY!  You\'ve run out of chance.  The correct word is %s.'%secret)
        break
    guess=input('Guess a LETTER (lowercase) : ')
    guess=guess[0]
    opened=checker(secret,guess)
input()
