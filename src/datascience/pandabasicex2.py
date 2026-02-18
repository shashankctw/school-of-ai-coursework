import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Select specific columns and filter rows

selected_columns = df[["species", "sepal_length"]]
print("Selected columns: \n", selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered rows: \n", filtered_rows)