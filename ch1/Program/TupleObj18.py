# Write a Python program to work with the different ways of creating tuple objects with suitable example programs

print( "Empty Tuple\n=====================================" )
t1 = ()
print( "Empty list : ", t1 )

print( "\nTuple with Element\n=====================================" )
lt1 = [1,2,3,'3w']
print( "Empty list : ", lt1 )

print( "\nTuple withot Parentheses\n=====================================" )
lt = 1,2,3,'3w',234.5
print( "Empty list : ", lt )

print( "\ncreate tuple using list\n=====================================" )
lt1 = ( 's', 'fgd', 'sd' )
print( "Empty list : ", lt1 )

print( "\ncreate tuple using range\n=====================================" )
lt1 = tuple(range( 1, 6 ) )
print( "Empty list : ", lt1 )