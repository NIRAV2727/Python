# ) Write a Python program to work with the following functions/methods which
# operates on lists in Python with suitable examples: i) list( ) ii) len( ) iii) count( ) iv)
# index ( ) v) append( ) vi) insert( ) vii) extend() viii) remove( ) ix) pop( ) x) reverse( )
# xi) sort( ) xii) copy( ) xiii) clear( )

lt = [ 1, 4, 2, 1, 2, 3.2, 4.54, 'a', 'fd' ]

l = [ 423, 456, 23, 6789, 1232, 873, 6, 436, 7587, 5647 ]

t = ( 1, 3.2, 4.54, 'a', 'fd' )
lt1 = list(t)
print( "Using list()\n==========================\nlt1 List : ", lt1 )

print( "\nUsing len()\n==========================\nlt List : ", len(lt) )

print( "\nUsing count('1')\n==========================\nlt1 List : ", lt.count(1) )

print( "\nUsing index()\n==========================\nlt List : ", lt.index( 'a' ) )

lt.append(78234)
print( "\nUsing append()\n==========================\nlt List : ", lt )

lt.insert(2,'dfji')
print( "\nUsing insert()\n==========================\nlt List : ", lt )

lt.extend( lt1 )
print( "\nUsing extend()\n==========================\nlt List : ", lt )

lt.remove('dfji')
print( "\nUsing remove()\n==========================\nlt List : ", lt )

lt.pop()
print( "\nUsing pop()\n==========================\nlt List : ", lt )

lt.reverse()
print( "\nUsing reverse()\n==========================\nlt List : ", lt )

l.sort()
print( "\nUsing sort()\n==========================\nl List : ", l )

lt1 = lt.copy()
print( "\nUsing copy()\n==========================\nlt1 List : ", l )

lt1.clear()
print( "\nUsing clear()\n==========================\nlt1 List : ", lt1 )