'''
Help generate boxplot / histogram for Descriptive Stat quiz
'''
import csv, seaborn as sns, pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

libr = "../../Datasets/librarians.csv"
#var = "tot_emp"

fight = "../../Datasets/fight-songs.csv"
var = "number_fights"

data = pd.read_csv(fight)

#_data = ages.filter(like="113", axis=0)
_data = data

#box = sns.boxplot(data=_data, orient='h', x=var)
#violin = sns.violinplot(data=_data, bw=0.3, x=var)
hist = sns.histplot(data=_data, bins=20, kde=False, x=var)

plt.show()