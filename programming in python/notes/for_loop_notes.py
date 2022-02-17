'''
Range
'''

# This prints 0 1 2 3 4
# NOTE: it doesn't print 5!
for i in range(5):
  print(i)

# Follow the worksheet to see what happens when you change the range.
# What's the difference?
range(2)
range(2,10)
range(2,10,2)

'''
The number of _parameters_ is important!
range(stop)
range(start, stop)
range(start, stop, step)

START at start
STOP BEFORE stop
ADD step each time (the interval / increment)
'''

'''
You can modify i inside the loop, too!
A great way to think about loops is to first figure
out what the range would output.
'''

# The following would print 5 6 7 8 9
for i in range(5): # for i in [0,1,2,3,4]
  print(i + 5)

# The "i" stands for "index" or "item"

# You don't need to use i inside the for loop!
for i in range(99):
  print("bye")

# PRINT ODD NUMBERS
for i in range(1,99,2):
  print(i)
# What would you change to make it print evens instead?

'''
Combining Loops with Functions
'''
def say_hi_more(n):
  for i in range(n):
    print("Hello")

say_hi_more(203) # How many times will "Hello" be printed?