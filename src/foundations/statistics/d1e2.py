import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

# Discrete random variable: Dice roll
outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6
plt.bar(outcomes, probabilities, color='blue', alpha=0.7)
plt.title('Probability Mass Function of a Fair Die')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.show()

# Continuous random variable: Uniform distribution
x = np.linspace(0, 1, 100)
pdf = uniform.pdf(x, loc=0, scale=1)
plt.plot(x, pdf, color='red')
plt.title('Probability Density Function of a Uniform Distribution')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()