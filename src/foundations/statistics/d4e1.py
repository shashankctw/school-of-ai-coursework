import numpy as np
from scipy.stats import ttest_1samp

# Sample data
data = [12, 14, 15, 16, 17, 18, 19]

# Null Hypothesis mean = 15
population_mean = 15

# Perform t-test
t_stat, p_value = ttest_1samp(data, population_mean)
print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value <= alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")