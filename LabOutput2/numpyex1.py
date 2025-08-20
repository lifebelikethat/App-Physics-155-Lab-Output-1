import numpy as np
import matplotlib.pyplot as plt

freq1 = 1
freq2 = 2


def angular_freq(freq):
    return 2 * np.pi * freq


omega1 = angular_freq(freq1)
omega2 = angular_freq(freq2)
t = np.arange(1, 5, 0.01)

f1list = []
f2list = []
f3list = []

for time in t:
    f1 = np.sin(omega1 * time)
    f2 = np.sin(omega2 * time)
    f3 = f1 * f2
    f1list.append(f1)
    f2list.append(f2)
    f3list.append(f3)

p1 = plt.figure()
plt.plot(t, f1list, label='f1')

p2 = plt.figure()
plt.plot(t, f2list, label='f2')

p3 = plt.figure()
plt.plot(t, f3list, label='f1*f2')

plt.show()
