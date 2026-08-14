# Write a Python program to work with type conversion functions.

a = 21
c = 's'
b = 2.3
d = "asdf"

print(int(a))
print(float(a))
print(chr(a))
print(str(a))

try:
    print(int(c))
except:
    print("Cannot convert 's' to int")

try:
    print(float(c))
except:
    print("Cannot convert 's' to float")

# print(chr(c))   # Invalid because chr() requires an integer

print(str(c))

print(int(b))
print(float(b))

try:
    print(chr(int(b)))      # Convert float to int first
except:
    print("Cannot convert float to character")

print(str(b))

try:
    print(int(d))
except:
    print("Cannot convert 'asdf' to int")

try:
    print(float(d))
except:
    print("Cannot convert 'asdf' to float")

try:
    print(chr(d))
except:
    print("Cannot convert string to character using chr()")

print(str(d))