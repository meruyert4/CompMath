import numpy as np

def Gauss_method(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    augmented_matrix = np.hstack((A, b))

    n = len(b)

    for i in range(n):
        max_row = i + np.argmax(abs(augmented_matrix[i:, i]))
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        # Check for zero pivot
        if abs(augmented_matrix[i, i]) < 1e-12:
            print("The system has no unique solution.")
            return None

        # Eliminate entries below the pivot
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:n], x[i + 1:])) / augmented_matrix[i, i]

    return x

# # Example usage
# A = [[1, 2, 1],
#      [0, 2, 5],
#      [3, 4, 1]]
# b = [4, 6, 7]
#
# solution = Gauss_method(A, b)
# if solution is not None:
#     print("Solution:", solution)