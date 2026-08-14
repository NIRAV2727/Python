# Write a Python script to sort (ascending and descending) a dictionary by value

my_dict = { 'apple': 50, 'banana': 20, 'orange': 40, 'grape': 10 }

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Order:", ascending)
print("Descending Order:", descending)