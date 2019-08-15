player_x=[]
player_o=[]
count=1
draw=True

def print_board(player_x,player_o):
    for row in range(1,4):
        for column in range(1,4):
            box=row*3+column-3
            if box in player_x:
                print(' x',end=' ')
            elif box in player_o:
                print(' o',end=' ')
            else:
                print(' _',end=' ')
        print()
def row_win(player):
    for row in range(1,4):
        win=True
        for column in range(1,4):
            box=row*3+column-3
            if box in player:
                win=win
            else:
                win=False
        if win==True:
            return win
    return win
def column_win(player):
    for column in range(1,4):
        win=True
        for row in range(1,4):
            box=row*3+column-3
            if box in player:
                win=win
            else:
                win=False
        if win==True:
            return win
    return win
def cross_win(player):
    win=True
    for row in range(1,4):
        column=row
        box=row*3+column-3
        if box in player:
            win=win
        else:
            win=False
            break
    if win==True:
        return win
    win=True
    for row in range(1,4):
        column=4-row
        box=row*3+column-3
        if box in player:
            win=win
        else:
            win=False
            break
    return win
def input_coor(player_x,player_o):
    while True:
        row=input('Choose which row? ')
        column=input('Choose which column? ')
        box=int(row)*3+int(column)-3
        if row in ['1','2','3'] and column in ['1','2','3']:
            if box in player_x or box in player_o:
               print('Cell occupied, input again:')
            else:
               break
        else:
            print('Invalid input, input again:')
    return box

print('Welcome to this Tic-Tac-Toe Game!')
while count<10:
    print_board(player_x,player_o)
    if count%2==1:
        if  row_win(player_o)==True or column_win(player_o)==True or cross_win(player_o)==True:
            draw=False
            print('Player O wins!')
            break
        else:
            print('Player X\'s turn:')
            player_x.append(input_coor(player_x,player_o))
    else:
        if  row_win(player_x)==True or column_win(player_x)==True or cross_win(player_x)==True:
            draw=False
            print('Player X wins!')
            break
        else:
            print('Player O\'s turn:')
            player_o.append(input_coor(player_x,player_o))
    count=count+1
if draw==True:
    print_board(player_x,player_o)
    print('Draw.')
input()
            
    
    
