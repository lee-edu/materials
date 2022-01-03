'''
Help generate histogram for Descriptive Stat quiz
'''
import csv, seaborn as sns, pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

ages = pd.read_csv('../../Datasets/congress-ages.csv')

#_data = ages.filter(like="113", axis=0)
_data = ages

#violin = sns.violinplot(data=ages, bw=0.3, x="age")
hist = sns.histplot(data=_data, bins=30, kde=False, x="age")

plt.show()