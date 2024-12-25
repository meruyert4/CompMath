import numpy as np

def Jacobi_method(A, b, x0, tol, max_iterations):
    n = len(b)
    x = x0.copy()

    for k in range(max_iterations):
        x_new = np.zeros_like(x)

        for i in range(n):
            # Calculate the sum of A[i, j] * x[j] for all j except i
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)

            # Update x_new[i]
            x_new[i] = (b[i] - s) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1

        x = x_new

    raise ValueError("Jacobi method did not converge within the maximum number of iterations")

# Example Usage
# if __name__ == "__main__":
#     A = np.array([[2, 1, 1],
#                   [1, 3, -1],
#                   [-1, 1, 2]], dtype=float)
#     b = np.array([6, 0, 3], dtype=float)
#     x0 = np.zeros_like(b)
#     tol = 1e-6
#     max_iterations = 100
#
#     try:
#         solution, iterations = Jacobi_method(A, b, x0, tol, max_iterations)
#         print(f"Solution: {solution}")
#         print(f"Converged in {iterations} iterations")
#     except ValueError as e:
#         print(e)
