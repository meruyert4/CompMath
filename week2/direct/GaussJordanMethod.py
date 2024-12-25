import numpy as np

def Gauss_jordan(A, b):
    # Combine A and b into the augmented matrix
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    augmented_matrix = np.hstack((A, b))

    n = len(b)

    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Partial pivoting: Swap rows to position the largest pivot element in the current row
        max_row = i + np.argmax(abs(augmented_matrix[i:, i]))
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        # Check for zero pivot
        if abs(augmented_matrix[i, i]) < 1e-12:
            print("The system has no unique solution.")
            return None

        # Scale the pivot row to make the pivot element 1
        augmented_matrix[i] /= augmented_matrix[i, i]

        # Eliminate entries in other rows
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    # Extract the solution vector from the last column of the augmented matrix
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
