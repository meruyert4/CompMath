def func(x):
    return x**3 - x - 1

def false_position(func, a, b):
    max_iter = 100
    tol = 1e-6
    if func(a) * func(b) >= 0:
        raise ValueError("the function must change its sign in interval [a,b] use proper values")

    for i in range(max_iter):
        # c = a - f(a) . (b-a) /[f(b) - f(a)]
        c = a - (func(a) * (b-a))/(func(b) - func(a))

        if abs(func(c)) < tol:
            print(f"Converged in {i + 1} iterations")
            return c

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("Max iterations reached without convergence")


a = 1
b = 2
root = false_position(func, a, b)
print(f"Root is: {root}")