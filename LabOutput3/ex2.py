import numpy as np
import matplotlib.pyplot as plt

x = 0.1 * np.linspace(1, 100)
y = []


def func(x):
    return (1-np.cos(x))/x**2


def new_func(x):
    return (2 * np.sin(x/2)**2 / x**2)


for num in x:
    y.append(func(num))


fig, ax = plt.subplots()

ax.scatter(x, y)
ax.set_xscale("log")

print(func(1.2e-8))
print(new_func(1.2e-8))
ax.grid(True)
plt.show()


"""
(a) Graph approaches 0.5 as x approaches 0.

(b) Limit of (1-cos(x))/x^2 as x approaches
0 is 1/2 using L'Hopital's Rule.

(c) Result gives 0.7709882115452477
which does not make sense since
it should approach 0.5

(d) New function gives 0.5
"""
