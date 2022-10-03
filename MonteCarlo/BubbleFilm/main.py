from audioop import avg
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import cm

# Make Wire
xs = []
ys = []
zs = []
z_freq = 2 # how many peaks in our perimeter wire

for theta in np.arange(-np.pi, np.pi, 0.01):
    xs.append(np.cos(theta))
    ys.append(np.sin(theta))
    zs.append(0.1*np.sin(z_freq*theta))

# Monte Carlo agents
num_points = 100
num_runs = 100000
actions = [(0.1, 0), (0, 0.1), (-0.1, 0), (0, -0.1)]
starting_xs = []
starting_ys = []
avg_boundary_height_hit = []
# TODO add incremental update rule for mean boundary height

for point in range(num_points):
    x, y = 2*np.random.random_sample() - 1 , 2*np.random.random_sample() - 1
    while x**2 + y**2 > 1:
        x, y = 2*np.random.random_sample() - 1 , 2*np.random.random_sample() - 1
    starting_xs.append(x)
    starting_ys.append(y)

    for run in range(num_runs):
        boundary_heights_hit = []
        while x**2 + y**2 < 1:
            action = random.sample(actions, 1)
            x += action[0][0]
            y += action[0][1]
        hit_angle = np.arctan2(y, x)
        boundary_heights_hit.append(0.1*np.sin(z_freq*hit_angle))
    # print(boundary_heights_hit)
    avg_boundary_height_hit.append(np.mean(boundary_heights_hit))
    # avg_boundary_heights_hit.append(0)
    


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)


ax.scatter(xs, ys, zs)
# ax.scatter(starting_xs, starting_ys, avg_boundary_height_hit, s=5, c=avg_boundary_height_hit)

# # Uncomment this for a surface plot that is slow, but looks cool
surf = ax.plot_trisurf(starting_xs, starting_ys, avg_boundary_height_hit, cmap=cm.jet, linewidth=0)
plt.show()