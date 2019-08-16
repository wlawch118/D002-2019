from random import randint
def opening(guess,secret):
    while True:
        opened=randint(1,3)
        if opened==guess:
            continue
        if opened==secret:
            continue
        break
    return opened
win_count=0
for time in range(0,100000):
    secret=randint(1,3)
    guess=randint(1,3)
    opened=opening(guess,secret)
    if guess==secret:
        win_count=win_count+1
    else:
        win_count=win_count
print('If you don\'t change your choice, the probability of winning will be %.1f percent.'%(win_count/1000.0))
win_count=0
for time in range(0,100000):
    secret=randint(1,3)
    guess=randint(1,3)
    opened=opening(guess,secret)
    new=[1,2,3]
    new.remove(guess)
    new.remove(opened)
    if new[0]==secret:
        win_count=win_count+1
    else:
        win_count=win_count
print('If you change your choice, the probability of winning will be %.1f percent.'%(win_count/1000.0))
