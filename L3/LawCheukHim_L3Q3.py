words=[ ]
target='aeiou'
for i in range(1,11):
    string=str(input('''%d. '''%i))
    for j in target:
        if ( string[0]==j ):
            words.append(string)
print(words)
input()
