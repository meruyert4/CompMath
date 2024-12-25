import numpy as np
def Cramer_method(A, b):
    # Convert inputs to numpy arrays
    A = np.array(A)
    b = np.array(b)

    # Compute the determinant of A
    det_A = np.linalg.det(A)

    if det_A == 0:
        print("The determinant of the coefficient matrix is zero. The system has no unique solution.")
        return None

    # Number of variables
    n = A.shape[0]

    # Initialize solution vector
    x = []

    # Compute each xi using Cramer's Rule
    for i in range(n):
        # Create a modified matrix by replacing the i-th column of A with b
        A_i = A.copy()
        A_i[:, i] = b

        # Compute the determinant of the modified matrix
        det_A_i = np.linalg.det(A_i)

        # Calculate xi
        x_i = det_A_i / det_A
        x.append(x_i)

    return x


# Example usage
# A = [[2, 3],
#      [4, 1]]
# b = [5, 11]
#
# solution = Cramer_method(A, b)
# if solution:
#     print("Solution:", solution)