year = input ( 'Please input the year\n' )
print ( 'Is %d a leap year?' %year )
if ( year%4 == 0 and year%100 != 0 ) :
    print ( 'Yes, it is a leap year' )
elif ( year%400 == 0 ) :
    print ( 'Yes, it is a leap year' )
else :
    print ( 'No, it isn\'t a leap year' )
