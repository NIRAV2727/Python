# Write a Python program to work with the control transfer statements in Python with
# suitable examples. i) break ii) continue iii) pass

for i in range(1,101) :
    if i > 50 :
        break
    elif i % 2 == 0 :
        continue
    else :
        print(i,end=" ")
        pass