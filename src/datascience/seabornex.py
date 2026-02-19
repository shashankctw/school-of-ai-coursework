# Create a Heatmap using Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Removing non-numeric columns for correlation calculation
df_numeric = df.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix
correation_matrix = df_numeric.corr()

# Plot Heatmap
sns.heatmap(correation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()