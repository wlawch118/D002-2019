from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
print("So Kevin is going to paid $%d.00." %(100*ceil(bill/100.0)))  
print("The cafe is giving %.2f to Kevin." %(100-(bill%100))) 
print("Each one should give %.2f to Kevin." %(bill/people))

number = int(1)
while (number <= 100):
    if (number%7==0 or number%10==7):
        print('X', end= ' ')
    else:
        print(number, end= ' ')    
    number = number + 1
print("\nGame Over.")


from random import randint

number = randint(1,6)
print("I got a %d" % number)
count = 1
while number != 6 : 
    number=randint(1,6)
    print("I got a %d" % number)
    count = count + 1

print("Oh, it takes me %d times to get a 6!!!" % count)
input()
