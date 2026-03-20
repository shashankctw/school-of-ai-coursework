from scipy.stats import ttest_ind

# Data from two groups
group1 = [5, 7, 8, 6, 9, 10, 7]
group2 = [4, 6, 5, 7, 8, 6, 5]

# Perform the t-test
t_statistic, p_value = ttest_ind(group1, group2)
print(f"T-statistic: {t_statistic}, P-value: {p_value}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")