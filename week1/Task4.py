import math

# Define the given equations as functions
def eq1(x):  # x^3 - x - 1 = 0
    return x**3 - x - 1

def eq2(x):  # x - cos(x) = 0
    return x - math.cos(x)

def eq3(x):  # e^(-x) - x = 0
    return math.exp(-x) - x

def eq4(x):  # x^3 + x^2 + x + 7 = 0
    return x**3 + x**2 + x + 7

def eq5(x):  # x^2 + 4*sin(x) = 0
    return x**2 + 4*math.sin(x)

def eq6(x):  # cos(x) = x * e^x  →  cos(x) - x*e^x = 0
    return math.cos(x) - x * math.exp(x)

# Derivatives for Newton-Raphson Method
def eq1_derivative(x):  # Derivative of x^3 - x - 1
    return 3*x**2 - 1

def eq2_derivative(x):  # Derivative of x - cos(x)
    return 1 + math.sin(x)

def eq3_derivative(x):  # Derivative of e^(-x) - x
    return -math.exp(-x) - 1

def eq4_derivative(x):  # Derivative of x^3 + x^2 + x + 7
    return 3*x**2 + 2*x + 1

def eq5_derivative(x):  # Derivative of x^2 + 4*sin(x)
    return 2*x + 4*math.cos(x)

def eq6_derivative(x):  # Derivative of cos(x) - x*e^x
    return -math.sin(x) - math.exp(x) - x*math.exp(x)

# Bisection Method
def bisection(f, a, b, tol=1e-6, max_iter=100):
    i = 0
    if f(a) * f(b) >= 0:
        print("Bisection method fails. Root may not be bracketed.")
        return None, i
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c, i + 1
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
    return c, i

# Newton-Raphson Method
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    i = 0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
        i += 1
    return x, i

# Secant Method
def secant(f, x0, x1, tol=1e-6, max_iter=100):
    i = 0
    for _ in range(max_iter):
        if abs(f(x1) - f(x0)) < 1e-12:
            return x1, i + 1
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_new - x1) < tol:
            return x_new, i + 1
        x0, x1 = x1, x_new
        i += 1
    return x1, i
# Solve the equations
methods = ["Bisection", "Newton-Raphson", "Secant"]
equations = [(eq1, eq1_derivative, "x^3 - x - 1 = 0", 1, 2),
             (eq2, eq2_derivative, "x - cos(x) = 0", 0, 1),
             (eq3, eq3_derivative, "e^(-x) - x = 0", -1, 1),
             (eq4, eq4_derivative, "x^3 + x^2 + x + 7 = 0", -3, -2),
             (eq5, eq5_derivative, "x^2 + 4*sin(x) = 0", -2, -1),
             (eq6, eq6_derivative, "cos(x) = x * e^x", 0, 1)]

print(f"{'Equation':<30} {'Bisection':<25} {'Newton-Raphson':<25} {'Secant':<25}")
print(f"{'':<30} {'iteration':<20} {'iteration':<30} {'iteration':<40}")

for eq, eq_der, label, a, b in equations:
    bisect_root, iter_bi = bisection(eq, a, b, tol=1e-6)
    newton_root, iter_new = newton_raphson(eq, eq_der, (a+b)/2 + 0.1, tol=1e-5)
    secant_root, iter_se = secant(eq, a + 0.1, b - 0.1, tol=1e-4)
    print(f"{label:<30} {iter_bi:<10} {bisect_root:<15.10f} {iter_new:<10} {newton_root:<15.10f} {iter_se:<10} {secant_root:<15.10f}")