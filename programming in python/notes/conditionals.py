num = int(input("Give me a number:\n"))
if 10 <= num and num <= 20: # 10 <= num <= 20
	print("This number is between 10 and 20")
else:
	print("This number is not between 10 and 20")

"""
Question 2
"""
# code for question 2

# Example code:
# == (double equal) checks for equality
if 3 == 4:
	print("Math is wrong!")









word = input("What is your favorite word?")
if len(word) > 8:
	print("This word is longer than 8 letters")
else:
	print("This word is under 8 letters")

"""
Pseudocode (it's a way of thinking about code)
get a word from the other person
count how many letters are in the word
if there are more than 8 letters:
	say "that's a long word"
otherwise:
	say that's not a long word
"""


"""
Question 3
"""
num = float(input("Give me a number"))
# ValueError: cannot read literal as int with base 10: -1.05
#if not num == -1.05: #num != -1.05
if num == -1.05:
	print("I do not like this number")
else:
	print("This is my favorite number")


# For saying whether a number is even
"""pseudocode
ask user for number
if number is even:
	print this is even
else:
	print this is odd
"""
"""
= assignment operator
it assigns a value to a variable
-----------
== comparison operator
checks if both sides are equal / the same
-----------
!= not equals operator
we read ! (the exclamation mark) as "not"
checks if both sides are not equal / the same
"""
not True # !true, !raining, !gameOver

num = int(input("Give me a number"))
if num % 2 == 1: # checks if even # modulus %
	print("This number is even")
else:
	print("This number is odd")

# modulus % calculates the remainder 
# when dividing 2 numbers

"""Example:
19 % 4 >>> 3
because 19 / 4 = 4 R 3
so remainder of 3
so 19 % 4 >>> 3
"""

"""
More examples of mod
23 % 5 >>> 3
23 / 5 = 4 R 3


8 % 2 >>> 0
8 / 2 = 4 R 0

24 % 2 >>> 0

25 % 2 >>> 1

"""

"""
elif is short for else if
"""
if grade >= 97 and grade <= 100:
	print("A+")
elif grade >= 94 and grade <= 96:
	print("A")
elif grade >= 90 and grade <= 93:
	print("A-")
else:
	print("Not A")


if raining:
	bring_umbrella()
elif is_cold:
	bring_jacket()
else:
	sit_in_park()


if tired:
	go_to_sleep()
elif had_coffee:
	do_some_work()
else:
	try_to_sleep()

# You can **nest** if statements
# Nest just means put an if statement 
# inside another if statement
if hungry:
	go_eat_early()
elif thirsty_for_water: # B
	if have_water: #F
		drink_water() #G
	else:
		get_water() #H
elif have_work: # C
	do_some_work() # D
else:
	sleep() # E






