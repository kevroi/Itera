import numpy as np
import matplotlib.pyplot as plt
import nSphere

ns = [2**ii for ii in range(4,20)]
dimensions = range(2,7)

vols = [np.pi, np.pi * 4/3, np.pi**2 * 1/2, np.pi**2 * 8/15, np.pi**3 * 1/6]


# Integration error for unit n-spheres
for i in range(len(dimensions)):
    errors = []
    for n in ns:
        mc_vol = nSphere.integrate(n, dimensions[i], radius=1)
        errors.append(abs(vols[i]-mc_vol))
    plt.plot(ns, errors, label = f'D = {i}')

# Data for 1/sqrt(N)
theo = [1/np.sqrt(n) for n in ns]
plt.plot(ns, theo, color='black', label='$1/{\sqrt{N}}$')

#Plotting
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of points (N)')
plt.ylabel('Error')
plt.title('Monte Carlo Integration Errors for different n-sphere volumes')
plt.legend()
plt.show()