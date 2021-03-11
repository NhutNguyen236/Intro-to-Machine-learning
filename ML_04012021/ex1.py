# Exercise 01: Count occurenece of each element from file ex1.txt
from collections import Counter

# Read file ex1
a_file = open("ex1.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

# new string
new_str = ""
new_str = new_str.join(contents_split)
listStr = new_str.split()
print(Counter(listStr))


