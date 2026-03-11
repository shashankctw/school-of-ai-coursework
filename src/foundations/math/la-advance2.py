import numpy as np

A = np.array([[4, -2], [5, 1]])

eigvals, eigvecs = np.linalg.eig(A)

print("Eigenvalues: \n", eigvals)
print("Eigenvectors: \n", eigvecs)