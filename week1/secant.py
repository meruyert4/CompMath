import math
import numpy


def f(x):
    return x ** 2 - 16


def secant(x0, x1, e, N):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('i-%d, x2 = %0.6f f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('out of maximum step')
            break

        condition = abs(f(x2)) > e
    print('\nRoot is: %0.8f' % x2)


secant(1, 10, 0.000001, 100)