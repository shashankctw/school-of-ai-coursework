# Create a 3X3 Matrix and Perform operations on it

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix: \n", matrix)

# Transpose of the Matrix
transpose = matrix.T
print("Transpose of the Matrix: \n", transpose)

another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Addition: \n", matrix + another_matrix)
print("Multiplication: \n", matrix * another_matrix)