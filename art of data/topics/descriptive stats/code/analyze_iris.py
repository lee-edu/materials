'''
Help generate histogram for Descriptive Stat worksheet
'''
import csv, seaborn as sns, pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import scipy

iris = pd.read_csv('../../Datasets/iris.csv')

#mean
def mean(ls):
  return sum(ls)/len(ls)

#std dev
def standard_deviation(ls):
  _mean = mean(ls)
  _sum = 0
  for x in ls:
    _sum += (x-_mean)**2
  return (_sum/(len(ls)-1))**.5

#corr
def correlate(xs, ys):
  n = len(xs)
  sx = standard_deviation(xs)
  sy = standard_deviation(ys)
  _x = mean(xs)
  _y = mean(ys)
  _sum = 0
  for i in range(0,n):
    _sum += (xs[i] - _x) * (ys[i] - _y)
  return (1/(n-1)) * (1/(sx*sy)) * _sum

#regression line
def regress(xs, ys):
  sx = standard_deviation(xs)
  sy = standard_deviation(ys)
  _x = mean(xs)
  _y = mean(ys)
  m = correlate(xs, ys) * (sy/sx)
  return (m, _y - m * _x)

test = iris.groupby('species')['petal-width'].describe()
print(test)

'''
#---------------------
versicolor = iris[iris['species'] == "Iris-versicolor"]
petal_lengths = list(versicolor['petal-length'])
petal_widths = list(versicolor['petal-width'])
regression_line = scipy.stats.linregress(petal_lengths, petal_widths)
print(regression_line.slope)
print(regression_line.intercept)
print(regress(petal_lengths, petal_widths))

print(iris.describe())

_data = iris[iris['species'] == "Iris-versicolor"]

#hist = sns.histplot(data=petal_lengths, bins=20, kde=False)
#box = sns.boxplot(data=petal_lengths, orient='h')
#violin = sns.violinplot(data=_data, bw=0.3, x="petal-length")

scatter = sns.regplot(data=_data, x='petal-length', y='petal-width')

plt.show()
'''