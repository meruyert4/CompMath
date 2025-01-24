import numpy as np

def divided_diff_table(x, y, n):
    table = np.zeros((n, n))
    table[:, 0] = y

    # Calculate the divided differences
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table


def newton_polynomial(x, y, x_value):
    n = len(x)
    table = divided_diff_table(x, y, n)
    coeff = table[0, :]

    # Evaluate the polynomial at x_value
    result = coeff[0]
    product_term = 1
    for i in range(1, n):
        product_term *= (x_value - x[i - 1])
        result += coeff[i] * product_term

    return result


x = [1, 2, 4, 7]
y = [1, 8, 64, 343]

x_value = 5
result = newton_polynomial(x, y, x_value)

print(f"Value of the polynomial at x = {x_value}:", result)
