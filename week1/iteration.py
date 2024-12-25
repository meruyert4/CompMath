import time
def g(x):
    return (x + 1) ** (1 / 3)

def f(x):
    return x ** 3 - x - 1

start_time = time.time()

x0 = 1.5
TOL = 0.000001
NMAX = 6

print("Iteration\t  x_n\t\t  f(x_n)")

for itr in range(1, NMAX + 1):
    x1 = g(x0)  # Compute the next approximation
    print(f'{itr}\t\t{x1}\t\t{f(x1)}')  # Print iteration details

    # Check for convergence based on the tolerance
    if abs(x1 - x0) < TOL:
        print("\nThe approximate root is:", x1)
        break

    x0 = x1  # Update the value for the next iteration
else:
    print("\nThe method did not converge within the maximum number of iterations.")

end_time = time.time()

# Display the computation time
print(f"Time: {end_time - start_time}")
