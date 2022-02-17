import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re

books = pd.read_csv("../../Datasets/bestsellers.csv")

#Bar Plot section
# Trim book names (too long otherwise)
books['Name'] = books['Name'].apply(lambda x: re.split(":|-", x)[0])

# Extract top 5 books w/ most reviews in 2019
_data = books[books['Year'] == 2019].nlargest(5, 'Reviews')
# DATAFRAME_SELECTION.METHOD_TO_APPLY()

#_data.to_csv("../../Datasets/bestsellers_modelA.csv", index=False)

# Shuffle
#bar = sns.barplot(data=_data, x='Name', y='Reviews')
_data = _data.sort_values("Reviews")
bar = sns.barplot(data=_data, y='Name', x='Reviews', color="teal")
plt.xticks(np.linspace(0, 90000, num=10))
plt.show()

'''
_data = _data.sample(frac=1)
dot = sns.stripplot(data=_data, x='Reviews', y='Name', color="black")

plt.grid(alpha=0.5)
plt.show()
'''

''' Grouped bar plots
_data = books
grouped = sns.countplot(data=_data, x="Year", hue="Genre")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()
'''