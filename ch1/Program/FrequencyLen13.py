# Write a Python program to work with the count frequency
# of characters in a given file.

file = open("demo.txt", "r")

data = file.read()
frequency = {}

for ch in data:
    if ch == "\n" or ch == " ":
        continue
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print( "Character Frequency:" )

for ch in frequency:
    print( ch, ":", frequency[ch] )

file.close()