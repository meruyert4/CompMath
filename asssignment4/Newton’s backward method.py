def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def newton_backward_interpolation(x_values, y_values, x):
    # Step size (h)
    h = x_values[1] - x_values[0]

    # Calculate p
    n = len(x_values) - 1
    p = (x - x_values[n]) / h

    # Difference Table
    diff_table = [y_values[:]]  # Initialize with y values

    for i in range(1, len(x_values)):
        diff_row = []
        for j in range(len(diff_table[i - 1]) - 1):
            diff_row.append(diff_table[i - 1][j + 1] - diff_table[i - 1][j])
        diff_table.append(diff_row)

    # Newton's Backward Formula
    y_interp = y_values[-1]  # Last value of y
    for i in range(1, len(x_values)):
        term = (p * (p + 1)) if i > 1 else p
        for j in range(2, i + 1):
            term *= (p + j - 1)
        y_interp += (term / factorial(i)) * diff_table[i][-1]

    return y_interp


# Example: Interpolating using Newton's Backward Formula
x_vals = [100, 150, 200, 250, 300, 350, 400]
y_vals = [10.63, 13.03, 15.04, 16.81, 18.42, 19.90, 21.27]

# Interpolating y for x = 410 (near the end of the table)
x_interp = 410
y_result = newton_backward_interpolation(x_vals, y_vals, x_interp)
print(f"The interpolated value of y for x = {x_interp} is {y_result:.2f}")
