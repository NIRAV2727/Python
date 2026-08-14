# Write a Python program to print each line of a file in reverse order

f = open("demo1.txt", "r")

for i in f:
    print( i.strip()[::-1] )

f.close()