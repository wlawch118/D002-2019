count=0
for a in range(1,13):
    for b in range(a+2,15):
        for c in range(b+2,17):
            for d in range(c+2,19):
                for e in range(d+2,21):
                    count=count+1
print('Number of combinations is %d.'%count)
