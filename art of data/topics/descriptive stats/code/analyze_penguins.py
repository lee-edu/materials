#%%
import pandas as pd
import seaborn as sns

penguins = pd.read_csv("../../../Datasets/penguins.csv")

gentoo = penguins[penguins["species"] == "Gentoo"]
gentoo

#%%
# Create Histogran of Gentoo Bill Lengths
sns.histplot(data=gentoo, x="bill_length_mm", palette="crest")

#%%
# Get max of Gentoo bill lengths
gentoo["bill_length_mm"].iloc[gentoo["bill_length_mm"].idxmax()]

#%%
# Get measures of Gentoo bill lengths
gentoo.describe()
# %%
# Create box plot of gentoo bill lengths
sns.boxplot(data=gentoo, x="bill_length_mm")

# %%
# Create violin plot of gentoo bill lengths
sns.violinplot(data=gentoo, x="bill_length_mm")
