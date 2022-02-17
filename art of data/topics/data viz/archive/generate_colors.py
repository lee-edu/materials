import random

# proportions
# {9: 1,1,3 10: 3,1,1 11: 1,3,1, 12: 2,2,1}

grades = {
  9: ["red", "blue"] + ["yellow"] * 3,
  10: ["red"] * 3 + ["blue", "yellow"],
  11: ["red", "yellow"] + ["blue"] * 3,
  12: ["red", "red", "blue", "blue", "yellow"]
}

print("grade,favorite_color")
for i in range(2500):
  grade = random.randint(9,12)
  color = random.choice(grades[grade])
  print("{},{}".format(grade,color))
