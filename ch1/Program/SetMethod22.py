# Write a Python program to work with the following functions/methods which
# operates on sets in Python with suitable examples: i) add( ) ii) update( ) iii) copy( )
# iv) pop( ) v) remove( )vi)discard( ) vii) clear( ) viii) union() ix) intersection( ) x)
# difference( )

st1 = { 1, 2,3 }
s11 = {10, 20, 30}
s2 = {30, 40, 50}

print("Before add()     : ", st1 )
st1.add(4)
print("After add()      : ", st1 )

st1.update([23,43,2,23])
print("After updation   : ", st1 )

s1 = st1.copy()
print("After Copy       : ", s1 )

st1.pop()
print("After pop        : ", st1 )

st1.remove(23)
print("After remove     : ", st1 )

st1.discard(435)
print("After Discard    : ", st1 )

s3 = s11.union(s2)
print("union()          : ", s3 )

s3 = s11.intersection(s2)
print("intersection()   : ", s3 )

s3 = s11.difference(s2)
print("difference()     : ", s3 )

print( "After clear()    : ", st1.clear() )