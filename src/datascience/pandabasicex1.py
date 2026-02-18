import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore Structure of the Dataset
print("first 5 rows of the dataset: \n", df.head())
print("last 5 rows of the dataset: \n", df.tail())

print(df.describe())
