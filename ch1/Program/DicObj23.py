# Write a Python program to work with the different ways of creating dictionary objects with suitable example programs.

print( "Empty dictionary\n=====================================" )
st1 = {}
print( "Empty dictionary : ", st1 )

print( "\ndictionary with Element\n=====================================" )
st2 = { "name":"nds", "address":"dfhg" }
print( "dictionary : ", st2 )

print( "\nusing dict()\n=====================================" )
d1 = dict(name="Rahul", age=20, city="Surat")
print( "using dict() : ", d1 )

print( "\nUsing zip\n=====================================" )
keys = ["name", "age", "city"]
values = ["Rahul", 20, "Surat"]
d1 = dict(zip(keys, values))
print( "Using zip : ", d1 )