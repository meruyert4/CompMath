def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45

def weddles_rule(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("n must be a multiple of 6")

    h = (b - a) / n
    sum_y = 0

    for i in range(0, n, 6):
        sum_y += (f(a + i * h) + 5 * f(a + (i + 1) * h) + f(a + (i + 2) * h) +
                  6 * f(a + (i + 3) * h) + f(a + (i + 4) * h) + 5 * f(a + (i + 5) * h) + f(a + (i + 6) * h))

    return (3 * h / 10) * sum_y

a, b = 0, 4
n = 12

result = weddles_rule(f, a, b, n)
print("Approximate integral", result)