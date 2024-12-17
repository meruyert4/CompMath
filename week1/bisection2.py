import math

def func(x):
    return math.exp(x) - x ** 2

def bisection(a, b, stages=7):
    if func(a) * func(b) >= 0:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
        return None

    print(f"Stage |    a     |    b     |    c     |  f(c)")
    print("-------------------------------------------------")

    for i in range(1, stages + 1):
        c = (a + b) / 2

        print(f"{i:^5} | {a:^8.4f} | {b:^8.4f} | {c:^8.4f} | {func(c):^8.4f}")

        # Check if c is the root
        if func(c) == 0.0:
            print("Exact root found!")
            return c

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    print(f"\nApproximate root after {stages} stages: {c:.4f}")
    return c


a = -2
b = 0
bisection(a, b, stages=7)
