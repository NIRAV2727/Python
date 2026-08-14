# Write a function that takes a character (i.e. a string of length 1) and returns True if it
# is a vowel, False otherwise.

def vowel(ch) :
    vow = "aeiouAEIOU"
    if ch in vow :
        return True
    else :
        return False

char = input( "Enter only single character for vowel or not : " )
print(vowel(char))