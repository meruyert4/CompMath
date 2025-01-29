def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n
    sum_y = f(a) + f(b)

    for i in range(1, n, 2):
        sum_y += 4 * f(a + i * h)

    for i in range(2, n - 1, 2):
        sum_y += 2 * f(a + i * h)

    return (h / 3) * sum_y

a, b = 0, 4
n = 4

result = simpsons_rule(f, a, b, n)
print("Approximate integral", result)