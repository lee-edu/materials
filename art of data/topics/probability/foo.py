#%%
import random
import math

N = 100000


inside = 0
for _ in range(N):
  x = random.random() #random.uniform(0,1)
  y = random.random()
  if math.dist([x, y], [0,0]) < 1:
    inside += 1

4 * inside / N
#%%
from random import random
import math

N = 1000
points = [(random(), random()) for _ in range(N)]
num_inside = sum(1 for (x,y) in points if math.dist([x,y], [0,0]) < 1)

4 * num_inside / N

#%%
L = []
for i in range(5):
  if i % 2 == 0:
    L.append(1)

L = [1 for i in range(5) if i % 2  == 0]