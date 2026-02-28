import numpy as np

# Identity matrix
I = np.eye(3)
A = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
print("Identity matrix: \n", np.dot(A, I))

# Diagonal matrix
D = np.diag([1, 2, 3])
Z = np.zeros((3, 3))
print("Diagonal matrix: \n", D)
print("Zero matrix: \n", Z)