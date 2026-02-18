import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40]
})

df2 = pd.DataFrame({
    "ID": [3, 4, 5, 6],
    "Score": [85, 90, 95, 80]
})

print("Dataset 1:\n", df1)
print("\nDataset 2:\n", df2)

merged = pd.merge(df1, df2, on="ID", how="inner")
print("\nMerged Dataset: \n", merged)

merged["Score_percentage"] = (merged["Score"] / 100) * 100
print("\nTransformed Dataset:\n", merged)