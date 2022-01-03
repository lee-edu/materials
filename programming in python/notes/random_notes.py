"""
Randomness
"""
import random

# Generate a random number
x = random.randint(-10,10)
print("You see " + x + " ogres.")

# Percent Chance
# random() generates between 0 and 1
if random.random() < .33:
	print("Heads!")
else:
	print("Tails!")

# Choose randomly from a list
print("You're gonna get a day of the week.")
day = ["Monday", "Tuesday", "Wednesday"]
print("You got....")
print(random.choice(day))

