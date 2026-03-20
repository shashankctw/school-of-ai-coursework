# Perform a Chi-Square Test

from scipy.stats import chi2_contingency

# Contingency table
data = [[10, 20, 30],[20, 30, 40]]

# Perform the Chi-Square Test
chi2, p, dof, expected = chi2_contingency(data)
print(f"Chi-Square Test - Chi2: {chi2}, P-value: {p}, Expected Frequencies: {expected}")