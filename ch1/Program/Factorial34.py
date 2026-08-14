# Write a recursive function to print the factorial for a given number

def factorial (num2) :
    if num2 == 0 or num1 == 1 :
        return 1
    else :
        return num2 * factorial(num2 - 1)

num1 = int(input( "Enter Number : " ))
print(factorial(num1))