import numpy as np

def Gauss_seidel(A, b, x0, tolerance=0.002, max_iterations=100):
    n = len(b)
    x = x0.copy()
    iter = 0

    for k in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            # Compute the sums for the formula
            sum1 = sum(A[i][j] * x[j] for j in range(i))         # Updated values
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n)) # Previous values

            # Update xi
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        # counting iterations
        iter = iter + 1

        # Check for convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            break

    return x, iter

# Example: Solve the given system
# A = np.array([[20, -1, 2],
#               [-3, 20, 1],
#               [2, -3, 20]])
# b = np.array([17, -18, 25])
# x0 = np.array([0.0, 0.0, 0.0])  # Initial guess
#
# # Solve the system
# solution = Gauss_seidel(A, b, x0)
#
# # Print the solution
# print("Solution:", solution)
