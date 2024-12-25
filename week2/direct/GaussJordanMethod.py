import numpy as np

def Gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    augmented_matrix = np.hstack((A, b))

    n = len(b)

    for i in range(n):
        max_row = i + np.argmax(abs(augmented_matrix[i:, i]))
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        if abs(augmented_matrix[i, i]) < 1e-12:
            print("The system has no unique solution.")
            return None

        augmented_matrix[i] /= augmented_matrix[i, i]

        for j in range(n):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    x = augmented_matrix[:, -1]
    return x

# Example usage
# A = [[1, 1, 1],
#      [2, -3, 4],
#      [3, 4, 5]]
# b = [9, 13, 40]
#
# solution = Gauss_jordan(A, b)
# if solution is not None:
#     print("Solution:", solution)
