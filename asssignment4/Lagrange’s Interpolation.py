def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0

    for i in range(n):
        # Calculate the Lagrange basis polynomial L_i(x)
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


# Example: Evaluate f(9) using Lagrange's formula
x_values = [5, 7, 11, 13, 17]
y_values = [150, 392, 1452, 2366, 5202]
x_interp = 9

# Interpolating f(x) at x = 9
f_9 = lagrange_interpolation(x_values, y_values, x_interp)
print(f"The interpolated value of f(9) is: {f_9:.2f}")
