def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)

    for i in range(1, n):
        sum += 2 * f(a + i * h)

    return (h / 2) * sum


a, b = 0, 10
n = 4
result = trapezoidal_rule(f, a, b, n)
print("Approximate integral:", result)
