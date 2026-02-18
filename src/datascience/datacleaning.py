import pandas as pd
import numpy as np

# Create a sample Dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve'],
    'Age': [25, 30, np.nan, 35, 28],
    'Score': [80, 70, 95, np.nan, 85],
}
df = pd.DataFrame(data)

print("Original Dataset:\n", df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].interpolate()

df = df.rename(columns={'Name': 'Full Name', 'Age': 'Age (Years)', 'Score': 'Score (Points)'})
print ("\nCleaned Dataset:\n", df)