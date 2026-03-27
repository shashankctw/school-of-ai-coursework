import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


# Load the dataset
url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

contingency_table = pd.crosstab(df['smoker'], df['time'])


# Perform the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")

# Interpret the results
alpha = 0.05
if p <= alpha:
    print("Reject the null hypothesis: There is a significant association between smoking status and time of day.")
else:
    print("Fail to reject the null hypothesis: There is no significant association between smoking status and time of day.")
    
    