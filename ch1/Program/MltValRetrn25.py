# Write a Python program to return multiple values at a time using a return statement.

def arithmeticOperation ( num1, num2 ) :
    add =  num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    return add, sub, mul, div

a, s, m, d = arithmeticOperation( 10, 2 )
print("addition        : ", a )
print("subsctraction   : ", s )
print("multiplication  : ", m )
print("division        : ", d )
