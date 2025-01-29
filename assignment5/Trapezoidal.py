import numpy as np

def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # Step size
    sum_y = f(a) + f(b)

    for i in range(1, n):
        sum_y += 2 * f(a + i * h)

    return (h / 2) * sum_y


a, b = 0, 4  # Integrate from 0 to 2
n = 12  # Number of trapezoids
result = trapezoidal_rule(f, a, b, n)
print("Approximate integral:", result)
