# Conduct T-Tests
# Perform one-sample, two-sample, and paired t-tests
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel

# One-sample t-test
data = [12, 15, 14, 10, 8]
population_mean = 10
t_statistic, p_value = ttest_1samp(data, population_mean)
print(f"One-sample T-Test - T-statistic: {t_statistic}, P-value: {p_value}")

# Two-sample t-test
group1 = [12, 15, 14, 10, 8]
group2 = [10, 9, 11, 8, 7]
t_statistic, p_value = ttest_ind(group1, group2)
print(f"Two-sample T-Test - T-statistic: {t_statistic}, P-value: {p_value}")

# Paired t-test
pre_test = [12, 15, 14, 10, 8]
post_test = [14, 16, 15, 12, 9]
t_statistic, p_value = ttest_rel(pre_test, post_test)
print(f"Paired T-Test - T-statistic: {t_statistic}, P-value {p_value}")
