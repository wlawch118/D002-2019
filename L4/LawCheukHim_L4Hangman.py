from random import randint
#edit word here
dictionary=['hangman','rhythm','python','programming','word','game','welcome','secret','guessing','printed',
            'inputs','users','enrichment','learning','studies','repeat','github','request','random','functional',
            'looping','letters','desktop','computer','barns','course','lecturer','lesson','tasks','powering',
            'kevin','william','algorithm','criteria','definition','highlight','random','declare','range']
secret=dictionary[randint(0,len(dictionary))]
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
def result(secret,opened,wrong):
    win=True
    for i in range(0,len(secret)):
        if i in opened:
            opened=opened
        else:
            win=False
    return win

print('Welcome to the HANGMAN game!')
while True:
    printer(secret,opened)
    print('WRONG letters : ',end='')
    for i in range(0,len(wrong)):
        print(wrong[i],end=' ')
    print()
    win=result(secret,opened,wrong)
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
