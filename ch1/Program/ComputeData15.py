# Write a Python program to compute the number of characters, words and lines in a
# file

fl = open( "demo1.txt","r" )
rd = fl.read()

char = len(rd)
word = len(rd.split())
line = len( rd.splitlines() )

print( "Number of character : ", char )
print( "Number of word      : ", word )
print( "Number of line      : ", line )