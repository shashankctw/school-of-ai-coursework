import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#Inspect the dataset
print(df.info())
print(df.describe())

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Filter data: Passengers in 1st class
first_class = df[df['Pclass'] == 1]
print("First class passengers: \n", first_class.head())

# Bar chart: Survival rate by class
survival_by_class = df.groupby('Pclass')['Survived'].mean()
survival_by_class.plot(kind='bar', color='blue')
plt.title('Survival Rate by Class')
plt.ylabel('Survival Rate')
plt.show()

# Histogram: Age distribution
sns.histplot(df['Age'], bins=20, kde=True, color='green')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Age vs Fare
plt.scatter(df['Age'], df['Fare'], alpha=0.5, color='red')
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()