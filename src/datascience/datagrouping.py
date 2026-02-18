import pandas as pd

data = {
    "Class": ["A", "A", "B", "B", "C", "C"],
    "Score": [85, 90, 78, 82, 92, 88],
    "Age": [25, 30, 22, 28, 35, 32]
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

grouped = df.groupby("Class").mean()
print(grouped)
