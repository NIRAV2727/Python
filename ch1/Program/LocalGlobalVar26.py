# Write a Python program to demonstrate Local and Global variables.

#global variable
num1 = 10

def fun() :
    # local variable
    num2 = 20
    print( "num1 : ", num1 )
    print( "num2 : ", num2 )

fun()
print( "num1 : ", num1 )
# print( "num2 : ", num2 )