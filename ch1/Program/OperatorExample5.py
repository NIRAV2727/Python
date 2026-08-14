# Write a Python program to work with the following Operators in Python with
# suitable examples.
# i) Arithmetic Operators
# ii) Relational Operators
# iii) Assignment Operator
# iv) Logical Operators
# v) Bit wise Operators
# vi) Ternary Operator

print( "Arithmetic Operators....\n================================================" )
num1 = 10
num2 = 4
print( "Sum            : ", num1 + num2 )
print( "Substraction   : ", num1 - num2 )
print( "Multiplication : ", num1 * num2 )
print( "Division       : ", num1 / num2 )
print( "Modulo         : ", num1 % num2 )

print( "\nRelational Operators....\n================================================" )
num3 = 31
num4 = 42
print( "num3 is big               : ", num3 > num4 )
print( "num4 is big               : ", num3 < num4 )
print( "num3 is big or equal      : ", num3 >= num4 )
print( "num4 is big or equal      : ", num3 <= num4 )
print( "num3 & num4 are same      : ", num3 == num4 )
print( "num3 & num4 are not equal : ", num3 != num4 )

print("\nAssignment Operators....\n================================================")

num1 = 678
num2 = 73

num1 = 13
print("Assign for num1         : ", num1)

num1 += 32
print("Add and assign          : ", num1)

num1 = 13
print("Assign for num1         : ", num1)

num1 -= 3
print("Subtract and assign     : ", num1)

num1 = 13
num1 *= 2
print("Multiply and assign     : ", num1)

num1 = 13
num1 /= 2
print("Divide and assign       : ", num1)

num1 = 13
num1 %= 5
print("Modulus and assign      : ", num1)

num1 = 13
num1 //= 5
print("Floor divide and assign : ", num1)

num1 = 13
num1 **= 2
print("Power and assign        : ", num1)

print( "\nLogical Operators....\n================================================" )
num3 = 31
num4 = 42
num1 = 87
print( "AND operator : ", num3 > num4 and num3 > num1 )
print( "OR operator  : ", num4 < num3 or num4 < num1 )
print( "NOT operator : ", not ( num1 > num4 and num1 < num3) )

print( "\nBit wise Operators....\n================================================" )
num1 = 10
num2 = 4
print( "Bitwise AND   : ", num1 & num2 )
print( "Bitwise OR    : ", num1 | num2 )
print( "Bitwise XOR   : ", num1 ^ num2 )
print( "Bitwise NOT   : ",  ~num2 )
print( "Left Shift    : ", num1 << num2 )
print( "Right Shift   : ", num1 >> num2 )

print( "\nTernary Operators....\n================================================" )
a = 10
b = 20
result = a if a > b else b
print( "Big value : ", result )