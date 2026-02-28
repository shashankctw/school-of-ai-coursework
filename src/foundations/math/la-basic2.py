import numpy as np

# Create matrix and vector
M = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
v = np.array([5, 6, 7])

# matrix-vector multiplication
result = np.dot(M, v)
print("matrix-vector multiplication: \n", result)