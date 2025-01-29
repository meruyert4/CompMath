def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45

def booles_rule(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("n must be a multiple of 4")

    h = (b - a) / n
    sum_y = 7 * (f(a) + f(b))

    for i in range(1, n, 4):
        sum_y += 32 * (f(a + i * h) + f(a + (i + 3) * h))  # Terms 1 & 3
    for i in range(2, n, 4):
        sum_y += 12 * f(a + i * h)  # Terms 2
    for i in range(4, n, 4):
        sum_y += 14 * f(a + i * h)  # Terms 4

    return (2 * h / 45) * sum_y

a, b = 0, 4
n = 4

result = booles_rule(f, a, b, n)
print("Approximate integral:", result)
