def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    sum_y = f(a) + f(b)

    for i in range(1, n):
        sum_y += 2 * f(a + i * h)

    return (h / 2) * sum_y


a, b = 0, 4
n = 12
result = trapezoidal_rule(f, a, b, n)
print("Approximate integral:", result)
