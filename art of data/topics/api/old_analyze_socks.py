#%%
import csv
from collections import Counter
socks = None
with open("../../Datasets/socks.csv", encoding="utf-8-sig") as f:
    socks = list(csv.DictReader(f))

#%%
import pandas as pd
socks_df = pd.read_csv("../../Datasets/socks.csv")

#%%
# Find sock with most variations
# Count variations
variation_counts = {}
for sock in socks:
    name = sock["Name"]
    if name not in variation_counts:
        variation_counts[name] = 0
    variation_counts[name] += 1

# Find max variation
most_variations = (0, [])
for sock in variation_counts:
    count = variation_counts[sock]
    if count > most_variations[0]:
        most_variations = (count, [sock])
    elif count == most_variations[0]:
        most_variations[1].append(sock)

most_variations

#%%
# Use pandas to check correct answer for most variations
v_counts = socks_df.groupby("Name").count().reset_index()
most_variations[1] == v_counts.loc[v_counts["Variation"] == v_counts["Variation"].max()]["Name"].to_list()


# %%
# Find counts of each color
color_counts = {}
for sock in socks:
    c1 = sock["Color 1"]
    c2 = sock["Color 2"]
    color_counts[c1] = color_counts.get(c1, 0) + 1
    if c1 != c2:
        color_counts[c2] = color_counts.get(c2, 0) + 1
color_counts

# %%
# Use pandas to check correctness of color counts
