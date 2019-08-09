ans=0
a=1
while a<=57:
    b=1
    while b<=(58-a):
        c=1
        while c<=(59-a-b):
            d=60-a-b-c
            if ans<(a*b+b*c+c*d):
                ans=(a*b+b*c+c*d)
                ansa=a
                ansb=b
                ansc=c
                ansd=d
            c=c+1
        b=b+1
    a=a+1
print(ans,ansa,ansb,ansc,ansd)
