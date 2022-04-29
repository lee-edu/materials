'''
Lists
'''

# How do you store multiple things?
card1 = 1
card2 = 2
card3 = 3

'''
What if you had 20 numbers? 200?
You don't want to have to write 200 variables.

A List is a collection of items.
It is one variable that can contain many things
'''

cards = [1,2,3,4,5]

'''
Every list has ELEMENTS / ITEMS.
Each item has a number / position called the INDEX.
We ACCESS individual elements using their INDEX.
'''

#index		0		   1        2         3
fruits = ["apple", "banana", "cherry", "apple"]

fruits[2] #>>> "cherry"
fruits[3] #>>> "apple"
fruits[1] #>>> "banana"

print("I ate this fruit: " + fruits[0])

'''
An INDEX can be negative to start from the _end_ of the list.
'''
fruits[-1] #>>> "apple"
fruits[-2] #>>> "cherry"

'''
A SLICE is a section of a list
'''
#index   0  1  2  3
fives = [5,10,15,20]

fives[1:2] #>>> [10]
fives[1:3] #>>> [10,15]
fives[0:3] #>>> [5,10,15]

##### CodingBat #####

def cutoff_sleeves(L):
  #return L[1:-1]
  last_index = len(L) - 1
  return L[1:last_index]
