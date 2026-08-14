# Write a Python program to work with the various ways of accessing the string.
# i) By using Indexing (Both Positive and Negative) ii) By using Slice Operator

str = "1234567890"

print( "By Indexing\n============================" )
print( "str[-1] : ", str[-1] )
print( "str[-4] : ", str[-4] )
print( "str[-9] : ", str[-9] )
print( "str[-7] : ", str[-7] )
print( "str[2]  : ", str[2] )
print( "str[6]  : ", str[6] )
print( "str[1]  : ", str[1] )

print( "By Slice Operator\n============================" )
print( "str[:]       : ", str[:] )
print( "str[0:6]     : ", str[0:6] )
print("str[-1:-9:-1] : ", str[-1:-9:-1])
print( "str[1:10:3]  : ", str[1:10:3] )



