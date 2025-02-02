import numpy as np
import math

def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    h = x_values[1] - x_values[0]

    # Create the difference table
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values

    for col in range(1, n):
        for row in range(n - col):
            diff_table[row, col] = diff_table[row + 1, col - 1] - diff_table[row, col - 1]
            # print(diff_table)

    print(diff_table)
    # Calculate p
    p = (x - x_values[0]) / h

    # Interpolate y using the formula
    y = y_values[0]
    factorial = 1
    for i in range(1, n):
        factorial *= i
        term = p
        for j in range(1, i):
            term *= (p - j)
        term *= diff_table[0, i] / factorial
        y += term

    return y

x_values = [2, 3, 4, 5]
y_values = [8, 27, 64, 125]
x = 9
print(9**3)
result = newton_forward_interpolation(x_values, y_values, x)
print(f"Interpolated value at x = {x}: {result}")
