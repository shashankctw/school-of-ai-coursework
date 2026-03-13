# Task 1 : Implement the Mathamatical formula for Linear regression

import numpy as np


# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add bias term to feature matrix
X_b = np.c_[np.ones((100, 1)), X]

# Initialize parameters
theta = np.random.randn(2, 1)
learning_rate = 0.1
iterations = 1000


def predict(X, theta):
    return np.dot(X, theta)

# Task 2 : Use Gradient Descent to optimise the model parameters

def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        gradient = (1/m) * np.dot(X.T, (np.dot(X, theta) - y))
        theta -= learning_rate * gradient
    return theta

# Task 3 : Calculate evaluation metrics

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)


# Perform Gradient descent
theta_optimized = gradient_descent(X_b, y, theta, learning_rate, iterations)

# Predictions and evaluations
y_pred = predict(X_b, theta_optimized)
mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimized Parameters (theta):", theta_optimized.flatten())
print("Mean Squared Error:", mse)
print("R-squared:", r2)