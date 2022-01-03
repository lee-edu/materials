'''
Randomly generate a csv file w/ ice cream flavor preferences
'''
import random

grades = [9,10,11,12]
flavors = {
  'vanilla': 0.3,
  'chocolate': 0.5,
  'strawberry': 0.2
}

print("id,grade,flavor")

for i in range(20):
  _id = i+1
  grade = random.choice(grades)
  flavor = random.choices(list(flavors.keys()), list(flavors.values()))[0]
  print("{},{},{}".format(_id, grade, flavor))
