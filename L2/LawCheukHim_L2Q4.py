ans=0
for a in range(0,61):
    for b in range(0,61-a):
        for c in range(0,61-a-b):
            d=60-a-b-c
            if ans<(a*b+b*c+c*d):
                ans=(a*b+b*c+c*d)
                ansa=a
                ansb=b
                ansc=c
                ansd=d
print(ans)
input()
