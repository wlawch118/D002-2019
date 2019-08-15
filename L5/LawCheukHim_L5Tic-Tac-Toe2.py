cells=[['_','_','_'],['_','_','_'],['_','_','_']]
count=1
draw=True


def printcell(cells):
    print("-" * 12)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 12)

def check_col(cells,player):
    if player=='player_x':
        for i in range(0,3):
            if cells[0][i]==cells[1][i]==cells[2][i]=='x':
                return True
    else:
        for i in range(0,3):
            if cells[0][i]==cells[1][i]==cells[2][i]=='o':
                return True
    return False
def check_row(cells,player):
    if player=='player_x':
        for i in range(0,3):
            if cells[i][0]==cells[i][1]==cells[i][2]=='x':
                return True
    else:
        for i in range(0,3):
            if cells[i][0]==cells[i][1]==cells[i][2]=='o':
                return True
    return False
def check_diagonal(cells,player):
    if player=='player_x':
        if cells[1][1]==cells[2][2]==cells[0][0]=='x':
            return True
        if cells[0][2]==cells[1][1]==cells[2][0]=='x':
            return True
    else:
        if cells[1][1]==cells[2][2]==cells[0][0]=='o':
            return True
        if cells[0][2]==cells[1][1]==cells[2][0]=='o':
            return True
def input_coor(player):
    while True:
        row=int(input('Choose which row? '))-1
        column=int(input('Choose which column? '))-1
        if row in [1,2,0] and column in [1,2,0]:
            if cells[row][column]=='_':
               break
            else:
               print('Cell occupied, input again:')
        else:
            print('Invalid input, input again:')
    if player=='player_x':
        cells[row][column]='x'
    else:
        cells[row][column]='o'

print('Welcome to this Tic-Tac-Toe Game!')
while count<10:
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
            
    
    
