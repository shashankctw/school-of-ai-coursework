from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Analyze sepal_length
feature = ['sepal_length']
print(f"Skewness of {feature[0]}: {skew(df[feature])}")
print(f"Kurtosis of {feature[0]}: {kurtosis(df[feature])}")

# Visualize the distribution
sns.heatplot(feature, kde=True)
plt.title("Distribution of Sepal Length")
plt.show()