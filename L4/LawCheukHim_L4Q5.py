def printer(secret, opened):
    for i in range(0,len(secret)):
        if i in opened:
            print(secret[i],end=' ')
        else:
            print('_',end=' ')
    print()
printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
input()
