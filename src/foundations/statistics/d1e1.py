import numpy as np

# Simulate rolling a die 10,000 times
rolls = np.random.randint(1, 7, size=10000)

# Calculate probabilities
P_even = np.sum(rolls % 2 == 0) / len(rolls)
P_greater_than_4 = np.sum(rolls > 4) / len(rolls)

print(f"Probability of rolling an even number: {P_even}")
print(f"Probability of rolling a number greater than 4: {P_greater_than_4}")