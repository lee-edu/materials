import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris_path = "REPLACE"
iris_df = pd.read_csv(iris_path)

_data = iris_df

graph = sns.countplot(data=_data, x='species')
plt.xlabel("Iris Species")

plt.show()