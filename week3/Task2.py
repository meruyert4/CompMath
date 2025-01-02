import numpy as np
from scipy.linalg import lu, lu_solve, lu_factor

def inverse_using_lu(A):
    lu_piv = lu_factor(A)

    identity = np.eye(A.shape[0])

    A_inv = np.zeros_like(A, dtype=float)
    for i in range(A.shape[0]):
        A_inv[:, i] = lu_solve(lu_piv, identity[:, i])

    return A_inv

A = np.array([[50, 107, 36],
              [35, 54, 20],
              [31, 66, 21]], dtype=float)

A_inverse = inverse_using_lu(A)

print("Matrix A:")
print(A)
print("\nInverse of Matrix A:")
print(A_inverse)
