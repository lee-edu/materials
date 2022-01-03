# Functions
"""
The purpose of a function is to bundle code
Functions have two steps:
1) defining: write what you want to do
2) call: it to run the code
"""
# Defining the function
# Use underscores to separate words
def name_of_function():
	# the code you want the function to do
	pass

# Calling the function
name_of_function() 

def escaping_the_cave():
	print("You fell into a cave")
	print("You have to escape!")

if ran_away:
	escaping_the_cave()
else:
	escaping_the_cave()

#################################

# A function can have parameters

def check_input(question, valid_answers):
	answer = input(question)
	if answer in valid_answers:
		return answer
	else:
		return check_input(question, valid_answers)

# We are passing values into the parameters
answer = check_input("Choose A B or C", ["A", "B", "C"])

# A Python _list_ is a group of items
# We use square brackets to make a list
# And commas to separate items
example = ["A", "B", "C"]
example2 = [1, 2, 3, 4]


# Halfway through the game
color = check_input(
	"What is your favorite color?",
	["red", "blue", "green"])
# Color is guaranteed to be red, blue, or green

if color == "red":
	pass
elif color == "blue":
	pass
else: # color has to be green
	pass

########################################
def game_over():
	# Let player know they lost
	print("You lost the game.")
	# End the game
	exit() # exit closes the entire Python program


if color == "green":
	game_over()

def restart():
	# How could we restart?
	# Hint: put your entire game into a function
	pass
