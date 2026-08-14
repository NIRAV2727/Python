# Write a Python program to copy the contents of a file to another file.

f = open("demo1.txt","r")

rd = f.read()

file = open("demo2.txt","w")
file.write(rd)
file = open("demo2.txt","r")
rdd = file.read()
print(rdd)
file.close()