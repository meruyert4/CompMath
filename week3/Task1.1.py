import numpy as np

def givens_method(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()

    for j in range(n):
        for i in range(m - 1, j, -1):
            a, b = R[i - 1, j], R[i, j]
            r = np.sqrt(a ** 2 + b ** 2)
            if r == 0:
                continue
            c, s = a / r, -b / r

            G = np.eye(m)
            G[i - 1, i - 1], G[i - 1, i] = c, -s
            G[i, i - 1], G[i, i] = s, c

            R = G @ R
            Q = Q @ G.T

    return Q, R


A = np.array([
    [4, 1, 2, 3],
    [3, 4, 1, 2],
    [2, 3, 4, 1],
    [1, 2, 3, 4]
])

Q, R = givens_method(A)

print("Givens Method Result:")
print("Matrix A:")
print(A)
print("\nOrthogonal Matrix Q:")
print(Q)
print("\nUpper Triangular Matrix R:")
print(R)

print("\nVerification A ≈ QR:")
print(np.dot(Q, R))
print("\nVerification Q is orthogonal (Q^T Q ≈ I):")
print(np.dot(Q.T, Q))