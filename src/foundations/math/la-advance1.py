import numpy as np

A = np.array([[4, 2, 3], [3, 4, 5], [5, 6, 7]])

determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("determinant: \n", determinant)
print("inverse: \n", inverse)