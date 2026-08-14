# Write a Python program to work with the different ways of creating list objects with
# suitable example programs

print( "Empty List\n=====================================" )
lt1 = []
print( "Empty list : ", lt1 )

print( "\nList with Element\n=====================================" )
lt1 = [1,2,3,4,5,6]
print( "List : ", lt1 )

print( "\nList with different data type\n=====================================" )
lt1 = [1,2.2,'a',"fhsadkj"]
print( "List : ", lt1 )

print( "\nList with comprehensive\n=====================================" )
lt1 = [x for x in range(1, 6)]
print( "List : ", lt1 )

print( "\nNested List\n=====================================" )
lt1 = [ [1], [2.3], ['a'], ["df"] ]
print( "Nested list : ", lt1 )
