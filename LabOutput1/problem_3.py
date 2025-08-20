# Longest Collatz Sequence Problem 14
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


seq = []


def T(N):
    seq.append(N)  # append each time T(N) is called
    c0 = N
    c_TN = 1

    if N == c_TN:
        return seq

    # change values of c0
    elif c0 % 2 == 0:
        c0 = c0 / 2
        T(c0)

    elif c0 % 2 != 0:
        c0 = 3*c0 + 1
        T(c0)

    return seq


x_points = []
y_points = []

for i in range(1, 1000000):
    x_points.append(i)
    y = len(T(i))
    y_points.append(y)
    seq = []

index = y_points.index(max(y_points))
print(x_points[index])
#837799
#plt.scatter(x_points, y_points)
plt.show()
