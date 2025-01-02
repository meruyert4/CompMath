import numpy as np

def power_method(A, v, tolerance=1e-6, max_iterations=100):
    for _ in range(max_iterations):
        v_next = np.dot(A, v)
        v_next /= np.linalg.norm(v_next)
        if np.linalg.norm(v_next - v) < tolerance:
            break
        v = v_next
    eigenvalue = np.dot(v.T, np.dot(A, v)) / np.dot(v.T, v)
    return eigenvalue, v


A_for_eigen = np.array([[2, -1, 0],
                        [-1, 2, -1],
                        [0, -1, 2]], dtype=float)

v_initial = np.array([1, 0, 0], dtype=float)

eigenvalue, eigenvector = power_method(A_for_eigen, v_initial)

print("\nLargest Eigenvalue:")
print(eigenvalue)
print("\nCorresponding Eigenvector:")
print(eigenvector)
