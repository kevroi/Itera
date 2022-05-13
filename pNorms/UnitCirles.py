import math
import numpy as np
import matplotlib.pyplot as plt


ps = [0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 10.0, 100.0, 1000.0, 1000000.0]
xs = np.arange(-1.0, 1, 0.0001)
y_all = []

for p in ps:
    ys = [(abs(1.0)**p - abs(x)**p)**(1/p) for x in xs]
    y_all.append(ys)

for p, ys in zip(ps, y_all):
    plt.plot(xs, ys, label=p)
plt.legend(title='Value of p', loc=(1.04,0))

# Negative y-values
y_all = []

for p in ps:
    ys = [-(abs(1.0)**p - abs(x)**p)**(1/p) for x in xs]
    y_all.append(ys)

for p, ys in zip(ps, y_all):
    plt.plot(xs, ys, label=p)



plt.title("The Unit Circle in different 2-Dimensional $L^p$ spaces")
plt.gca().set_aspect('equal')
plt.show()