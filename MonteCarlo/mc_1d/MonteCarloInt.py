import numpy as np
import random
import matplotlib.pyplot as plt

# Limits of integration
a = 0.0
b = np.pi

# Number of strips
N = 1000

x = [random.uniform(a,b) for i in range(N)]
x.sort() # sort x values for plt.show()

y = np.sin(x)

result = (b-a) * sum(y) / N

f = plt.figure()
plt.title("Monte Carlo Integration evaluates this integral to be "+str(result))
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(a, b)

for xcoord, ycoord in zip(x,y):
    plt.vlines(xcoord, 0, ycoord)

plt.grid()


plt.show()


