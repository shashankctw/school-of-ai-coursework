import numpy as np

A = np.array([[9, 7, -2], [5, 3, 1], [8, 6, 7]])
U, S, V = np.linalg.svd(A)

print("U: \n", U)
print("Singular values: \n", S)
print("V Transpose: \n", V.T)

# Reconstructing the original matrix
Sigma = np.zeros((3,3))
np.fill_diagonal(Sigma, S)
A_reconstructed = U @ Sigma @ V.T

print("Reconstructed matrix: \n", A_reconstructed)