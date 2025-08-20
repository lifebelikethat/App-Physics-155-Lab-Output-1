import numpy as np
import matplotlib.pyplot as plt
import random

r = 1
theta = np.linspace(0, np.pi/2)
x = r * np.cos(theta)
y = r * np.sin(theta)

x_list = []
y_list = []

for i in range(1000):
    rand_x = random.choice(theta)
    rand_y = random.choice(theta)

    if rand_x**2 + rand_y**2 <= 1:
        x_list.append(rand_x)
        y_list.append(rand_y)
        
dots_inside = len(x_list)
print(f'{dots_inside} points are inside out of 1000 points')
plt.plot(x, y)
plt.scatter(x_list, y_list)
plt.show()
