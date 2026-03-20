from scipy.stats import f_oneway

# Data for groups
group1 = [12, 15, 14, 10, 8]
group2 = [10, 9, 11, 8, 7]
group3 = [14, 16, 15, 12, 9]

# Perform ANOVA
f_statistic, p_value = f_oneway(group1, group2, group3)
print(f"ANOVA - F-statistic: {f_statistic}, P-value: {p_value}")