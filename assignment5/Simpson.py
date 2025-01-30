def f(x):
    return x ** 3 + x ** 2 + 3 * x + 45

def simpson_rule_1_3(func, a, b, n):
    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * func(x)
        else:
            result += 4 * func(x)

    result *= h / 3
    return result

def simpson_rule_3_8(func, a, b, n):
    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            result += 2 * func(x)
        else:
            result += 3 * func(x)

    result *= 3 * h / 8
    return result

a, b = 0, 4
n = 4

res1 = simpson_rule_1_3(f, a, b, n)
print(f"1/3: {res1}")
res2 = simpson_rule_3_8(f, a, b, n)
print(f"3/8: {res2}")
