ans=0
for a in range(1,58):
    for b in range(1,59-a):
        for c in range(1,60-a-b):
            d=60-a-b-c
            if ans<(a*b+b*c+c*d):
                ans=(a*b+b*c+c*d)
                ansa=a
                ansb=b
                ansc=c
                ansd=d
print(ans,ansa,ansb,ansc,ansd)
input()
