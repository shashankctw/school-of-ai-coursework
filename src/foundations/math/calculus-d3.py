import numpy as np

# Define the gradient descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradients = (1/m) * np.dot(X.T, errors)
        theta -= learning_rate * gradients
    return theta

# Sample data
X = np.array([[1, 1], [1, 2], [2, 2]])
Y = np.array([1, 2, 3])
theta = np.array([0.5, 0.5])
learning_rate = 0.01
iterations = 1000

# Perform gradient descent
optimized_theta = gradient_descent(X, Y, theta, learning_rate, iterations)
print("Optimized parameters: ", optimized_theta)
