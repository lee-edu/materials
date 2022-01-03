# Lists
# A list is a group of things
# It uses [] and ,

fruits = ["apple", "banana", "orange"]

# Lists have a numbering to them
# This numbering is called index
# Indexes start at 0

# A good list name is plural

"""
Index     0      1       2
Fruits  apple  banana  orange
"""

fruits[0] # >>>> apple
fruits[2] # >>> orange

len(fruits) # >>> 3

###### Extra Optional Stuff #####
# Example of a for loop
for fruit in fruits:
	print(fruit)

# Don't do this!
foo = [5,1,2349,1]
for asdf in foo:
	print(asdf)

# Example of a range
range(1, 300) 
# All numbers from 1 -300
