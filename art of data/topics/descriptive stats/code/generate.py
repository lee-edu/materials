'''
Help generate plots for Correlation / Linear Regression wkst
'''
import csv, seaborn as sns, pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import random

data = {'x':[], 'y': []}

''' Generate scatterplots
data['x'] = np.random.randint(-10,10, size=40)
#data['y'] = data['x'] * 2 + np.random.randint(10, 40)
data['y'] = [x*2 + np.random.randint(10,30) for x in data['x']]
data['y'] = np.array(data['y'])

print(np.corrcoef(data['x'], data['y']))

scatter = sns.regplot(data=data, x='x', y='y', ci=None)
'''

data['x'] = np.linspace(0, 10)
data['y'] = data['x'] * -1.4 + 8

plt.plot(data['x'], data['y'])
plt.axis([0,10,0,10])
plt.show()