import pandas as pd

data = {
    "Department": ["HR", "HR", "IT", "IT", "Sales", "Sales"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Salary": [50000, 55000, 60000, 65000, 45000, 48000],
    "Experience": [5, 7, 3, 4, 6, 2]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)

grouped = df.groupby("Department").mean(numeric_only=True)

stats = df.groupby("Department").agg(
    {"Salary": ["mean", "min", "max"], "Experience": ["mean", "min", "max"]}
)

print(stats)