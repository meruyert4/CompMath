def f(x):
    return x ** 3 - x - 2


def bisection(a, b, tol, error_type='absolute', max_iter=100):
    if f(a) * f(b) > 0:
        print("Function values at the endpoints must have opposite signs!")
        return None

    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'c':<10} {'Error':<10}")
    x_old = a

    for i in range(1, max_iter + 1):
        # Midpoint
        c = (a + b) / 2

        if error_type == 'absolute':
            error = abs(c - x_old)
        elif error_type == 'relative':
            error = abs((c - x_old) / c)
        else:
            print("Invalid error type! Use 'absolute' or 'relative'.")
            return None

        print(f"{i:<5} {a:<10.6f} {b:<10.6f} {c:<10.6f} {error:<10.6f}")

        if error < tol:
            print("\nRoot approximation:", round(c, 6))
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        x_old = c

    print("\nMaximum iterations reached!")
    return c


a = 1.0
b = 2.0
tolerance = 1e-5

print("Using Absolute Error:")
bisection(a, b, tolerance, error_type='absolute')

print("\nUsing Relative Error:")
bisection(a, b, tolerance, error_type='relative')
