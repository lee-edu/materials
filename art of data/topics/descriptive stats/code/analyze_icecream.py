#%%
'''
Used to create diagrams for Descriptive Stat worksheet
'''
import csv, seaborn as sns, pandas as pd

flavor_counts = {}

with open('../../Datasets/icecream.csv', 'r') as f:
  data = csv.DictReader(f)
  for row in data:
    current_flavor = row['flavor']
    if current_flavor not in flavor_counts:
      flavor_counts[current_flavor] = 0
    flavor_counts[current_flavor] += 1

flavor_df = pd.DataFrame([flavor_counts], columns=flavor_counts.keys())

print(flavor_counts)
print(flavor_df)

chart = sns.barplot(data=flavor_df, palette="crest")
# %%
