# Write a Python program to work with the following functions/methods which
# operates on dictionary in Python with suitable examples: i) dict( ) ii) len( ) iii) clear( )
# iv) get( ) v) pop( )vi)popitem( ) vii) keys( ) viii) values() ix) items( ) x) copy( ) xi)
# update( )

d = dict(name="Rahul", age=20, city="Surat")
dd = dict(name="Rahul", age=20, city="Surat")

print( "Using dict()     : ", d )

print( "Keys             : ", d.keys() )

print( "Values           : ", d.values() )

print( "Items            : ", d.items() )

print( "Using len()      : ", len(d) )

print( "Using dd.clear() : ", dd.clear() )

print( "Using d.get()    : ", d.get("name") )

d.pop("age")
print( "Using d.pop()    : ", d )

pt = d.popitem()
print( "popitem          : ", pt )

d2 = d.copy()
print( "copy             : ", d2 )

d.update( { "city": "Surat", "age": 21 } )
print( "Updated          : ", d )



