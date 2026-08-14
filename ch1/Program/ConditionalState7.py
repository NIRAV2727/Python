#Write a Python program to work with the Conditional statements in Python with
# suitable examples. i) if statement ii) if else statement iii) if – elif – else statement


num1 = 2346
num2 = 243

print( "Example for normal if statement........ " )
if num1 < num2 :
    print( "Big number is : ", num1 )

print("\n================================\nExample for if-else statement........ " )
if num1 > num2 :
    print( "First number is big!!!!" )
else :
    print( "Second number is big!!!!" )

print("\n================================\nExample for if – elif – else statement........ ")
if num1 > num2 :
    print( "First number is big!!!!" )
elif num2 > num1 :
    print( "Second number is big!!!!" )
else :
    print( "Program Puro")