cells=[['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_']]
count=1
draw=True


def printcell(cells):
    print("-" * 27)
    for i in [5,4,3,2,1,0]:
        for j in range(0, 7):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 27)

def check_col(cells,player):
    if player=='player_x':
        for j in range(0,4):
            for i in range(0,6):
                if cells[i][j]==cells[i][j+1]==cells[i][j+2]==cells[i][j+3]=='x':
                    return True
    else:
        for j in range(0,4):
            for i in range(0,6):
                if cells[i][j]==cells[i][j+1]==cells[i][j+2]==cells[i][j+3]=='o':
                    return True
    return False
def check_row(cells,player):
    if player=='player_x':
        for i in range(0,3):
            for j in range(0,7):
                if cells[i][j]==cells[i+1][j]==cells[i+2][j]==cells[i+3][j]=='x':
                    return True
    else:
        for i in range(0,3):
                for j in range(0,7):
                    if cells[i][j]==cells[i+1][j]==cells[i+2][j]==cells[i+3][j]=='o':
                        return True
    return False
def check_diagonal(cells,player):
    if player=='player_x':
        for j in range(0,4):
            for i in range(0,3):
                if cells[i][j]==cells[i+1][j+1]==cells[i+2][j+2]==cells[i+3][j+3]=='x':
                    return True
        for j in range(3,7):
            for i in range(0,3):
                if cells[i][j]==cells[i+1][j-1]==cells[i+2][j-2]==cells[i+3][j-3]=='o':
                    return True
    else:
        for j in range(0,4):
            for i in range(0,3):
                if cells[i][j]==cells[i+1][j+1]==cells[i+2][j+2]==cells[i+3][j+3]=='x':
                    return True
        for j in range(3,7):
            for i in range(0,3):
                if cells[i][j]==cells[i+1][j-1]==cells[i+2][j-2]==cells[i+3][j-3]=='o':
                    return True
        return False
def input_coor(player):
    while True:
        col=int(input('Choose which column? '))-1
        if col in range(0,7):
            valid=False
            available=[]
            for i in range(0,6):
                if cells[i][col]=='_':
                    valid=True
                    available.append(i)
        else:
            print('Invalid input, input again:')
            continue
        if valid==False:
            print('Cells occupied, input again:')
            continue
        break
    if player=='player_x':
        cells[available[0]][col]='x'
    else:
        cells[available[0]][col]='o'

print('Welcome to this Connect 4 Game!')
while count<43:
    printcell(cells)
    if count%2==1:
        if  check_row(cells,'player_o')==True or check_col(cells,'player_o')==True or check_diagonal(cells,'player_o')==True:
            draw=False
            print('Player O wins!')
            break
        else:
            print('Player X\'s turn:')
            input_coor('player_x')
    else:
        if  check_row(cells,'player_x')==True or check_col(cells,'player_x')==True or check_diagonal(cells,'player_x')==True:
            draw=False
            print('Player X wins!')
            break
        else:
            print('Player O\'s turn:')
            input_coor('player_o')
    count=count+1
if draw==True:
    printcell(cells)
    print('Draw.')
input()
            
    
    
