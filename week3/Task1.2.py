import numpy as np


def householder_reflection(A):
    """QR decomposition using Householder reflections."""
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()

    for k in range(n):

        x = R[k:, k]

        norm_x = np.linalg.norm(x)

        if norm_x < 1e-10:
            continue

        e1 = np.zeros_like(x)
        e1[0] = 1
        v = x - norm_x * e1

        v_norm = np.linalg.norm(v)
        if v_norm != 0:
            v = v / v_norm
        else:
            continue

        H = np.eye(m)
        H_k = np.eye(len(x)) - 2 * np.outer(v, v)
        H[k:, k:] = H_k

        R = H @ R
        Q = Q @ H.T

    return Q, R


A = np.array([
    [4, 1, 2, 3],
    [3, 4, 1, 2],
    [2, 3, 4, 1],
    [1, 2, 3, 4]
])

Q, R = householder_reflection(A)

print("Matrix A:")
print(A)
print("\nOrthogonal Matrix Q:")
print(Q)
print("\nUpper Triangular Matrix R:")
print(R)