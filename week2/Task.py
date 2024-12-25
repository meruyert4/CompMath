import numpy as np

# Given system of equations
A = np.array([[3, -5, 47, 20],
              [11, 16, 17, 10],
              [56, 22, 11, -18],
              [17, 66, -12, 7]], dtype=float)

b = np.array([18, 26, 34, 82], dtype=float)


# Function to solve using Cramer's Rule
def cramer(A, b):
    n = len(b)
    det_A = np.linalg.det(A)

    if det_A == 0:
        raise ValueError("Matrix A is singular, no unique solution exists.")

    x = np.zeros(n)
    for i in range(n):
        A_copy = A.copy()
        A_copy[:, i] = b
        x[i] = np.linalg.det(A_copy) / det_A
    return x


# Function to perform Gaussian Elimination
def gaussian_elimination(A, b):
    n = len(b)
    # Augmenting matrix A with b
    Augmented = np.hstack((A, b.reshape(-1, 1)))

    # Forward elimination
    for i in range(n):
        max_row = np.argmax(np.abs(Augmented[i:n, i])) + i
        Augmented[[i, max_row]] = Augmented[[max_row, i]]

        for j in range(i + 1, n):
            ratio = Augmented[j, i] / Augmented[i, i]
            Augmented[j, i:] -= ratio * Augmented[i, i:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Augmented[i, -1] - np.dot(Augmented[i, i + 1:n], x[i + 1:n])) / Augmented[i, i]
    return x


# Function to perform Jacobi Method
def jacobi(A, b, tolerance=1e-10, max_iterations=100000):
    n = len(b)
    x = np.zeros(n)
    for iteration in range(max_iterations):
        x_new = np.zeros(n)
        for i in range(n):
            summation = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - summation) / A[i, i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Jacobi method did not converge within the maximum number of iterations.")


# Function to perform Gauss-Seidel Method
def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000000):
    n = len(b)
    x = np.zeros(n)
    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            summation = np.dot(A[i, :], x_new) - A[i, i] * x_new[i]
            x_new[i] = (b[i] - summation) / A[i, i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Gauss-Seidel method did not converge within the maximum number of iterations.")


# Function to perform Gauss-Jordan Method
def gauss_jordan(A, b):
    n = len(b)
    # Augment matrix A with vector b
    Augmented = np.hstack((A, b.reshape(-1, 1)))

    # Forward elimination to make the matrix diagonal
    for i in range(n):
        # Make the diagonal contain all 1s
        Augmented[i] = Augmented[i] / Augmented[i, i]

        # Eliminate the i-th column elements from other rows
        for j in range(n):
            if i != j:
                Augmented[j] -= Augmented[i] * Augmented[j, i]

    # The solution is the last column of the augmented matrix
    return Augmented[:, -1]


# Function to perform Relaxation (Successive Over-Relaxation or SOR)
def relaxation(A, b, omega=1.25, tolerance=1e-10, max_iterations=100000):
    n = len(b)
    x = np.zeros(n)
    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            summation = np.dot(A[i, :], x_new) - A[i, i] * x_new[i]
            x_new[i] = (1 - omega) * x_new[i] + (omega * (b[i] - summation) / A[i, i])

        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Relaxation method did not converge within the maximum number of iterations.")


# Solve using Cramer's Rule
try:
    x_cramer = cramer(A, b)
    print("Solution using Cramer's Rule:", x_cramer)
except ValueError as e:
    print("Cramer's Rule error:", e)

# Solve using Gaussian Elimination
x_gaussian = gaussian_elimination(A, b)
print("Solution using Gaussian Elimination:", x_gaussian)

# Solve using Jacobi Method
try:
    x_jacobi = jacobi(A, b)
    print("Solution using Jacobi Method:", x_jacobi)
except ValueError as e:
    print("Jacobi Method error:", e)

# Solve using Gauss-Seidel Method
try:
    x_gauss_seidel = gauss_seidel(A, b)
    print("Solution using Gauss-Seidel Method:", x_gauss_seidel)
except ValueError as e:
    print("Gauss-Seidel Method error:", e)

# Solve using Gauss-Jordan Method
x_gauss_jordan = gauss_jordan(A, b)
print("Solution using Gauss-Jordan Method:", x_gauss_jordan)

# Solve using Relaxation (SOR) Method
try:
    x_sor = relaxation(A, b)
    print("Solution using Relaxation Method:", x_sor)
except ValueError as e:
    print("Relaxation Method error:", e)
