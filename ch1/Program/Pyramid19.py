# Write Python programs to print the following Patterns:
# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6) :
    for j in range(i) :
        print(i,end=" ")
    print()
print("\n")

# A
# A B
# A B C
# A B C D
# A B C D E
for i in range(1,6) :
    for j in range(65,65+i) :
        print(chr(j),end=" ")
    print()
print("\n")

# *****
# ****
# ***
# **
# *
for i in range(6,1,-1) :
    for j in range(i-1) :
        print("*",end=" ")
    print()
print("\n")
