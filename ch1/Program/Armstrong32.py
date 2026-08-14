# Write a function to check if the input value is Armstrong or not.

def armstrong(nm):
    power = len(nm)
    total = 0

    for digit in nm:
        total = total + int(digit) ** power

    return total


val = input("Enter any NUMBER : ")
result = armstrong(val)

if result == int(val):
    print("Number is Armstrong")
else:
    print("Not Armstrong")