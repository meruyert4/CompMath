import numpy as np
import matplotlib.pyplot as plt


time = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
power = np.array([500, 480, 450, 600, 800, 950, 1000, 980, 920, 850, 700, 550, 500])

def trapezoidal_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    integral = y[0] + y[-1]

    for i in range(1, n):
        integral += 2 * y[i]

    return (h / 2) * integral

def simpsons_1_3_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    integral = y[0] + y[-1]

    for i in range(1, n, 2):  # odd
        integral += 4 * y[i]
    for i in range(2, n - 1, 2):  # even
        integral += 2 * y[i]

    return (h / 3) * integral


def simpsons_3_8_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    integral = y[0] + y[-1]

    # Sum terms based on index
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * y[i] #every 3rd index
        else:
            integral += 3 * y[i]

    return (3 * h / 8) * integral

trapezoidal_result = trapezoidal_rule(time, power)
simpsons_1_3_result = simpsons_1_3_rule(time, power)
simpsons_3_8_result = simpsons_3_8_rule(time, power)

print(f"Total energy consumption using Trapezoidal Rule: {trapezoidal_result:.2f} MWh")
print(f"Total energy consumption using Simpson's 1/3 Rule: {simpsons_1_3_result:.2f} MWh")
print(f"Total energy consumption using Simpson's 3/8 Rule: {simpsons_3_8_result:.2f} MWh")


plt.figure(figsize=(10, 6))
plt.plot(time, power, 'bo-', label="Power Consumption Data")
plt.fill_between(time, power, alpha=0.2, color='blue', label="Estimated Area")

plt.xlabel("Time (hours)")
plt.ylabel("Power (MW)")
plt.title("Power Consumption Over Time and Numerical Integration")
plt.legend()
plt.grid(True)

# Show plot
plt.show()