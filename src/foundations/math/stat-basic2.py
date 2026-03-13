from scipy.stats import ttest_ind

# Sample datasets
group1 = [2.1, 2.5, 3.6, 3.9, 4.2]
group2 = [1.8, 2.3, 3.0, 3.5, 4.0]

# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")