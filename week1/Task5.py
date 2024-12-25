def f(x):
    return x ** 3 - x - 2

def bisection(a, b, max_iter=7, error_type='absolute'):
    if f(a) * f(b) > 0:
        print("Function values at the endpoints must have opposite signs!")
        return None

    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'c':<10} {'Error':<10}")
    x_old = a  # Initialize old midpoint to the start of the interval

    for i in range(1, max_iter + 1):
        # Compute the midpoint
        c = (a + b) / 2

        # Compute the error
        if error_type == 'absolute': # Measures the actual distance between two successive approximations. Simpler and intuitive for most cases.
            error = abs(c - x_old)
        elif error_type == 'relative': # Measures the error as a proportion of the current approximation. Useful when dealing with very large or very small roots.
            error = abs((c - x_old) / c)
        else:
            print("Invalid error type! Use 'absolute' or 'relative'.")
            return None

        print(f"{i:<5} {a:<10.6f} {b:<10.6f} {c:<10.6f} {error:<10.6f}")

        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Update the old midpoint
        x_old = c

    print("\nRoot approximation after 7 iterations:", round(c, 6))
    return c


# Inputs
a = 1.0
b = 2.0

# Using Absolute Error
print("Using Absolute Error:")
bisection(a, b, max_iter=7, error_type='absolute')

# Using Relative Error
print("\nUsing Relative Error:")
bisection(a, b, max_iter=7, error_type='relative')
