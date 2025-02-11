import numpy as np

time = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
power = np.array([500, 480, 450, 600, 800, 950, 1000, 980, 920, 850, 700, 550, 500])

# trapezoidal rule
def trapezoidal_rule(x, y):
    n = len(x) - 1
    integral = 0
    for i in range(n):
        integral += (x[i+1] - x[i]) * (y[i+1] + y[i]) / 2
    return integral

# simpsone's rule
def simpsons_rule(x, y):
    n = len(x) - 1
    if n % 2 == 1:
        raise ValueError("invalid inteval: must be even interval")
    h = (x[-1] - x[0]) / n
    integral = y[0] + y[-1] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2])
    return integral * h / 3

trapezoidal_result = trapezoidal_rule(time, power)
simpsons_result = simpsons_rule(time, power)

print(f"Total energy consumption using Trapezoidal Rule: {trapezoidal_result:.2f} MWh")
print(f"Total energy consumption using Simpson's Rule: {simpsons_result:.2f} MWh")
