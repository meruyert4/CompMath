import numpy as np
def iterative_method(A, B, tolerance=1e-6, max_iterations=100):
    iter = 0
    I = np.eye(A.shape[0])
    for _ in range(max_iterations):
        E = np.dot(A, B) - I
        B = np.dot(B, I - E + np.dot(E, E))
        iter = iter+1
        if np.linalg.norm(E) < tolerance:
            break
    return B, iter


A = np.array([[1, 10, 1],
              [2, 0, 1],
              [3, 3, 2]], dtype=float)

B = np.array([[0.4, 2.4, -1.4],
              [0.14, 0.14, -0.14],
              [-0.85, -3.8, 2.8]], dtype=float)

refined_inverse, iter = iterative_method(A, B)

print("\nInitial Approximate Inverse B:")
print(B)
print("\nInverse of A:")
print(refined_inverse)
print(iter)