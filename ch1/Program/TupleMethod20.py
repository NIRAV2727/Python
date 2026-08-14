# Write a Python program to work with the the following functions/methods which
# operates on tuples in Python with suitable examples: i) len( ) ii) count( ) iii) index( )
# iv) sorted( ) v) min ( )vi)max( ) vii) cmp( ) viii) reversed( )

tp = ( 1, 2, 65, 78, 21, 4.5, 43.34, "fxc", 'r' )
t = ( 1,6,4,9786,45,54 )

ln = tp.__len__()
print( "len() : ", ln )

cn = tp.count('r')
print( "count() : ", cn )

ind = tp.index(4.5)
print( "index() : ", ind )

st = sorted(t)
print( "len() : ", st )

small = min(t)
print( "len() : ", small )

big = max(t)
print( "len() : ", big )

# st = cmp(tp,t)
# print( "len() : ", st )

rv = reversed(t)
print( "reversed() : ", tuple(rv) )