import numpy as np

def Relaxation_method(A, b, x0, omega, tolerance=1e-6, max_iterations=100):
    n = len(b)
    x = x0.copy()

    for k in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            sigma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sigma)

        # Check convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            return x, k + 1

    raise ValueError("Solution did not converge within the maximum number of iterations")

# Example usage
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]], dtype=float)

b = np.array([15, 10, 10, 10], dtype=float)
x0 = np.zeros(len(b))
omega = 1.25  # Relaxation factor

tolerance = 1e-6
max_iterations = 100

# try:
#     solution, iterations = Relaxation_method(A, b, x0, omega, tolerance, max_iterations)
#     print(f"Solution: {solution}")
#     print(f"Iterations: {iterations}")
# except ValueError as e:
#     print(e)
