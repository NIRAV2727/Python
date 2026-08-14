# Write the function for the Input number is Palindrome or not.

def palindrom (nm) :
    rev = 0
    while nm > 0 :
        digit = nm % 10
        rev = rev * 10 + digit
        nm = nm // 10
    return rev

num1 = int( input( "Enter NUMBER : "))
res = palindrom(num1)

if res == num1 :
    print( num1, " is Palindrom " )
else :
    print( num1, " not palindrom " )