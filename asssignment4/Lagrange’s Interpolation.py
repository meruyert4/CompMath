def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


x_values = [0, 1, 2, 3, 4]
y_values = [1, 1, 8, 27, 64]
x = 5

f_5= lagrange_interpolation(x_values, y_values, x)
print(f"The interpolated value of f(9) is: {f_5}")
