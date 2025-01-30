def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45


def weedle_rule(func, a, b, n):
    if n % 6 != 0:
        return None

    h = (b - a) / n
    result = 0

    for i in range(1, n):
        x = a + i * h
        if i % 6 == 1 or i % 6 == 5:
            result += 5 * func(x)
        elif i % 6 == 2 or i % 6 == 4:
            result += func(x)
        elif i % 6 == 3:
            result += 6 * func(x)
        elif i % 6 == 0:
            result += 2 * func(x)

    result *= 3 * h / 10
    return result

a, b = 0, 4
n = 12
result = weedle_rule(f, a, b, n)
print("Approximate integral:", result)