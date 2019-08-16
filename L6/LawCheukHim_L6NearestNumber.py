from math import *
inputs=[]
for i in range(0,10):
    inputs.append(int(input('%d . '%(i+1))))
min_diff=abs(inputs[0]-inputs[1])
ans1=inputs[0]
ans2=inputs[1]
for j in range(0,9):
    for k in range(j+1,10):
        if abs(inputs[j]-inputs[k])<min_diff:
            min_diff=abs(inputs[j]-inputs[k])
            ans1=inputs[j]
            ans2=inputs[k]
print('%d and %d are the nearest.' %(ans1,ans2))
    
