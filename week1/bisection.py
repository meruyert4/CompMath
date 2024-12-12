import numpy as np


def f(x):
    return np.exp(x) - x ** 2


def bisection(f, a, b, tol=1e-5, max_iter=7):
    iterates = []
    for _ in range(max_iter):
        c = (a + b) / 2
        iterates.append((a, b, c, f(c)))

        if abs(f(c)) < tol:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return iterates


a = 0
b = 2

iterates = bisection(f, a, b)

print("Stage | a     | b     | c     | f(c)")
for i, (a_val, b_val, c_val, f_val) in enumerate(iterates, 1):
    print(f"{i:5} |{a_val:6.2f} |{b_val:6.2f} |{c_val:6.2f} |{f_val:6.2f}")
