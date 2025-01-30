def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45

def boole_rule(func, a, b, n):
    if n % 4 != 0:
        return None

    h = (b - a) / n
    result = 7 * func(a)

    for i in range(1, n):
        x = a + i * h
        if i % 2 != 0:
            result += 32 * func(x)
        elif i % 2 == 0 and i % 4 != 0:
            result += 12 * func(x)
        else:
            result += 14 * func(x)

    result *= 2 * h / 45
    return result

a, b = 0, 4
n = 12
result = boole_rule(f, a, b, n)
print("Approximate integral:", result)