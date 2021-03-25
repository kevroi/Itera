import numpy as np
import matplotlib.pyplot as plt

n = 10000
T = 1.0 # max duration
N = 3 # number of dimensions, or number of particles moving along a single axis

times = np.linspace(0.0, T, n)
dt = times[1] - times[0]

# Assume the impulses on the particle cause a displacement
# dx, normally distributed about 0, with normalised with
# variance dt

# list of all displacements the particle will undergo
dx = np.sqrt(dt) * np.random.normal(size=(N, n-1))

# Initialise all coordinates to 0, or all particles to x=0
x0 = np.zeros(shape=(N, 1))
x = np.concatenate((x0, np.cumsum(dx, axis=1)), axis=1)

# print(np.cumsum(dx, axis=0))

if N == 3:
    ax = plt.axes(projection='3d')
    ax.scatter(0,0,0, color='r')
    ax.plot(x[0], x[1], x[2])
    ax.scatter(x[0][-1],x[1][-1],x[2][-1], color='cyan')
    plt.title(f'Brownian motion of a particle in 3D space for {T} seconds')
    plt.show()

else:
    for i in range(N):
        plt.plot(times, x[i])
    plt.title(f'{N} Brownian motions')
    plt.show()




