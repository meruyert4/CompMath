import numpy as np

import numpy as np

def Gauss_seidel(A, b, x0, tol, max_iterations, omega=1.25):
    n = len(b)
    x = x0.copy()

    for k in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))
            sum2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            # Apply relaxation factor omega
            x[i] = (1 - omega) * x[i] + omega * (b[i] - sum1 - sum2) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k + 1

    raise ValueError("Gauss-Seidel method did not converge within the maximum number of iterations")


# Example usage
# A = np.array([[20, -1, 2],
#                     [3, 20, -1],
#                     [2, -3, 20]], dtype=float)
# b = np.array([17, -18, 25], dtype=float)
# x0 = np.zeros_like(b)
#
# tol = 1e-3
# max_iterations = 100

# try:
#     solution, iterations = Gauss_seidel(A, b, x0, tol, max_iterations)
#     print(f"Solution: {solution}")
#     print(f"Converged in {iterations} iterations")
# except ValueError as e:
#     print(e)
