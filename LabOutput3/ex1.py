import numpy as np
import time

start_time = time.time()


def quadratic_bad(a, b, c):
    x_pos = ((-b + np.sqrt(b**2 - (4*a*c)))/2*a)
    x_neg = ((-b - np.sqrt(b**2 - (4*a*c)))/2*a)

    print(x_pos, x_neg)


"""
When b is positive, we take the negative root so that
we are adding 2 big negative numbers, and therefore
avoiding the catastrophic cancellation.
"""


def quadratic_good(a, b, c):
    if b > 0:
        x2 = (-b - np.sqrt(b**2 - 4*a*c))/2*a
        x1 = c / (a*x2)
    elif b < 0:
        x1 = (-b + np.sqrt(b**2 - 4*a*c))/2*a
        x2 = c / (a*x1)

    # x1 * x2 = c/a
    print(x1, x2)


quadratic_bad(1, 10**8, 1)
quadratic_good(1, 10**8, 1)

print(time.time() - start_time, end=' seconds \n')
