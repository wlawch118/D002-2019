# Edit the points of rectangles 1 and 2
# where a is the top left corner and c is the bottom right corner 
a1=[-3,1]
c1=[3,-1]
a2=[-1,3]
c2=[1,-3]

# Process
def adjust(point):
    point[1]=-point[1]
def check(a1,c1,a2,c2,dim,x,y):
    if a1[dim]<=a2[dim]<=c1[dim] or a1[dim]<=c2[dim]<=c1[dim]:
        analyse('1 over 2',dim,x,y)
        if a1[dim]<=a2[dim]<=c1[dim] and a1[dim]<=c2[dim]<=c1[dim]:
            analyse('2 in 1',dim,x,y)
    if a2[dim]<=a1[dim]<=c2[dim] or a2[dim]<=c1[dim]<=c2[dim]:
        analyse('1 over 2',dim,x,y)
        if a2[dim]<=a1[dim]<=c2[dim] and a2[dim]<=c1[dim]<=c2[dim]:
            analyse('1 in 2',dim,x,y)
def analyse(string,dim,x,y):
    if dim==0:
        x.append(string)
    else:
        y.append(string)
def result(x,y):
    if '1 in 2' in x and '1 in 2' in y:
        print('1 is inside 2')
    elif '2 in 1' in x and '2 in 1' in y:
        print('2 is inside 1')
    elif '1 over 2' in x and '1 over 2' in y:
        print('1 and 2 overlaps with each other')
x=[]
y=[]
adjust(a1)
adjust(c1)
adjust(a2)
adjust(c2)
check(a1,c1,a2,c2,0,x,y)
check(a1,c1,a2,c2,1,x,y)
result(x,y)
input()
