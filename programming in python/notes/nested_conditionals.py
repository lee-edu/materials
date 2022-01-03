""" Review """

# Booleans / boolean expressions
# A boolean is a data type that can store true / false

is_tired = False
have_work = True
busy = is_tired == have_work


# = assignment operator
# Evaluate the right hand side first
# Then assign the variable on the left


""" Boolean Operators """

# == equality operator
# checks if both operands 
# are equal to each other

# != not equal operator
# checks if both operands 
# are not equal to each other

# Examples
x = 3
y = 5
x == y >>> False
x != y >>> True

is_equals = x == y
# is_equals = False

foo = x != y
#foo = (x != y)
#foo = (3 != 5)
#foo = True

""" Nested Conditionals """

# Nested conditionals means an if statement
# nested inside another if statement

# Example
x = 25
if x < 14: 		# Group 1 if
	if x > 11: 	# Group 2 if
		print("A")
	elif x > 8:	# Group 2 elif
		print("E")
	else:		# Group 2 else
		print("B")
elif x > 9:		# Group 1 elif
	if x > 5:	# Group 3 if
		print("D")
else: 			# Group 1 else
	print("C")







