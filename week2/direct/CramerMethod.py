import numpy as np
def Cramer_method(A, b):
    A = np.array(A)
    b = np.array(b)

    det_A = np.linalg.det(A)

    if det_A == 0:
        print("The determinant of the coefficient matrix is zero. The system has no unique solution.")
        return None

    n = A.shape[0]

    x = []

    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b

        det_A_i = np.linalg.det(A_i)

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