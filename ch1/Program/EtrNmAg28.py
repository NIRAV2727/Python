# Write a program that asks the user to enter their name and their age. Print out a
# message addressed to them that tells them the year that they will turn 60 years old

name = input( "Enter Name : " )
age = int( input( "Enter Age : " ) )
result = ( age >= 60 )
if result :
    print( name + "Bhai Resting time start" )
else :
    print( "Go to Office" )