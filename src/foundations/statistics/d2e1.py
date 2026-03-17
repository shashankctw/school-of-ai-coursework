import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, uniform

# Gaussian distribution
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x), label='Gaussian')

# Binomial distribution
n, p = 10, 0.5
x = np.arange(0, n+1)
plt.bar(x, binom.pmf(x, n, p), alpha=0.7, label='Binomial')

# Poisson distribution
lam = 3
x = np.arange(0, 10)
plt.bar(x, poisson.pmf(x, lam), alpha=0.7, label='Poisson')

plt.title('Probability Distributions')
plt.legend()
plt.show()