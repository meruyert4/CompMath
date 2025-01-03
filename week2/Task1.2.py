from iteration import *
import numpy as np

# A = np.array([[3, -5, 47, 20],
#               [11, 16, 17, 10],
#               [56, 22, 11, -18],
#               [17, 66, -12, 7]], dtype=float)
#
# b = np.array([18, 26, 34, 82], dtype=float)

A = np.array([[20, -1, 2],
                    [3, 20, -1],
                    [2, -3, 20]], dtype=float)
b = np.array([17, -18, 25], dtype=float)

x0 = np.zeros_like(b)
tol = 1e-3
max_iterations = 100

def is_diagonally_dominant(A):
    ''' for every row of the matrix, the magnitude of the diagonal entry in a row is greater than or equal to the
    sum of the magnitudes of all the other (off-diagonal) entries in that row. '''
    n = len(A)
    for i in range(n):
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) <= row_sum:
            return False
    return True

print(is_diagonally_dominant(A))

x02 = np.array([0.0, 0.0, 0.0])

resGaussSeidel, iterGauss = Gauss_seidel(A, b, x02)
print("Result with Gauss Seidel Method: ", resGaussSeidel, "in iterations: ", iterGauss)

resJacob, iterJacob = Jacobi_method(A, b, x0, tol, max_iterations)
print("Result with Jacobi Method: ", resJacob, "in iterations: ", iterJacob)

