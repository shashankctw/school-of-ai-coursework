import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate Data
np.random.seed(42)
x = 2 * np.random.rand(100, 1) * 10
y = 3 * x + np.random.rand(100, 1) * 2

# Fit Linear Regression Model
model = LinearRegression()
model.fit(x, y)

# Get coefficients
slope = model.coef_[0][0]
intercept = model.intercept_[0]
r_squared = model.score(x, y)

# Visualize
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.legend()
plt.title(f'Linear Regression')
plt.show()