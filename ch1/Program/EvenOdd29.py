#  Enter the number from the user and depending on whether the number is even or odd,
# print out an appropriate message to the user.


number = int( input( "Enter any number : " ) )
result = ( number % 2 == 0 )

if result :
    print( number, " is EVEN" )
else :
    print( number, " is ODD" )