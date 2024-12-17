import math

def func(x):
    # return x ** 3 - x - 1
    # return x - math.cos(x)
    # return math.e ** (x * -1) - x
    # return x ** 3 + x ** 2+ x + 7
    # return x ** 2 + 4 * math.sin(x)
    return math.cos(x) - x * math.e ** x

def func_derivative(x):
    # return 3 * x ** 2 - 1
    # return 1 + math.sin(x)
    # return -1 * ((1 + math.e ** x)/math.e**x)
    # return 3 * x ** 2 + 2 * x + 1
    # return 2 * x + math.cos(x)
    return math.sin(x) * (-1) - math.e ** x - x * math.e ** x

def newton_raphson(initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    for i in range(max_iter):
        f_x = func(x)
        f_prime_x = func_derivative(x)

        if f_prime_x == 0:
            raise ValueError("Derivative is zero. No convergence possible.")

        x_new = x - f_x / f_prime_x

        print(f"Iteration {i + 1}: x = {x_new}, f(x) = {func(x_new)}")

        if abs(x_new - x) < tol:
            print(f"Converged in {i + 1} iterations.")
            return x_new

        x = x_new

    raise ValueError("Maximum iterations reached without convergence.")


# Example usage
if __name__ == "__main__":
    initial_guess = -1
    root = newton_raphson(initial_guess)
    print(f"Root: {root}")
