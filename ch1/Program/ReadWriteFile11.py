# Write a Python program to work with the read and write operations on a file.

file = open("demo1.txt","w")
file.write("hello\npython")

fl = open("demo.txt","r")
rd = fl.read()
print(rd)
fl.close()