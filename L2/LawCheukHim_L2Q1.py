n = input("Enter a positive integer except 1 : ")
prime=True
if n%2==0:
    prime=False
test=3
while test<=n**0.5:
    if n%test==0:
        prime=False
        break
    test=test+2
if n<=1:
    print('Wrong input')
elif n==2:
    print('Prime')
elif prime==True:
    print('Prime')
elif prime==False:
    print('Not prime')
