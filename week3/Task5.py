import math

import numpy as np

def jacobi_method(A, tolerance=1e-6, max_iterations=100):
    n = A.shape[0]
    V = np.eye(n)
    for _ in range(max_iterations):
        max_val = 0
        p, q = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j
        if max_val < tolerance:
            break
        theta = 0.5 * np.arctan2(2 * A[p, q], A[p, p] - A[q, q])
        c, s = np.cos(theta), np.sin(theta)
        J = np.eye(n)
        J[p, p], J[q, q] = c, c
        J[p, q], J[q, p] = s, -s
        A = np.dot(J.T, np.dot(A, J))
        V = np.dot(V, J)
    eigenvalues = np.diag(A)
    return eigenvalues, V

A = np.array([[1, math.sqrt(2), 2], [math.sqrt(2), 3, math.sqrt(2)], [2, math.sqrt(2), 1]])
eigenvalues, eigenvectors = jacobi_method(A)
print("Jacobi's Method Result:")
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
