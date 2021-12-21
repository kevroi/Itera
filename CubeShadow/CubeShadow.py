import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt


class Cube():
    def __init__(self, dim=3):
        # did not end up needing vertices
        self.vertices  = ((np.arange(2**dim)[:,None] & (1 << np.arange(dim))) > 0) - 0.5
        self.normvectors = np.array(
                                    [[ 1,  0,  0],
                                     [-1,  0,  0],
                                     [ 0,  1,  0],
                                     [ 0, -1,  0],
                                     [ 0,  0,  1],
                                     [ 0,  0, -1]]
                                    ) # normal vectors all go out from cubes volume


    def rotate(self):
        '''
        Randomly rotate the cube, using a rotation vector that points 
        along the axis of rotation with length equal to the rotation angle
        '''
        # Generate spherical polar coordinates of rotation vector
        # theta and phi are uniformly distributed across the surface of a sphere
        theta = np.arccos(2*np.random.uniform()-1) # polar angle
        phi = 2*np.pi*np.random.uniform() # azimuthal angle
        r = np.random.uniform(low=0, high=2*np.pi) # encodes rotaion amount

        cart_rot_vec = np.array(
                                [r*np.sin(theta)*np.cos(phi),
                                 r*np.sin(theta)*np.sin(phi),
                                 r*np.cos(theta)]
                                )

        # Create rotation vector 
        r = R.from_rotvec(cart_rot_vec)
        # Create Rotation matrix in Cartesian unit vector basis
        rot_mat = r.as_matrix()

        self.vertices = np.matmul(self.vertices, rot_mat)
        self.normvectors = np.matmul(self.normvectors, rot_mat)

    
    def calc_shadow(self):
        '''
        Returns shadow of the unit cube by adding projections from all faces 
        pointing upwards
        '''
        shade = 0
        up = np.array([0, 0, 1])
        for vector in self.normvectors:
            if vector[2] > 0:
                shade += np.dot(vector, up)

        return shade


def average_shadow(n):

    shades = np.zeros(n)

    for i in range(n):
        c = Cube()
        c.rotate()
        shades[i] = c.calc_shadow()

    return np.average(shades)


# Plotting
npoints=100
ns = np.logspace(0,4, npoints)
ys = []
yref = np.full(npoints, 1.46)
for n in ns:
    ys.append(average_shadow(int(n)))

plt.plot(ns, ys, c='blue', label='Average Shadow')
plt.plot(ns, yref, c='red', label='1.46 units$^2$')
plt.xscale('log')
plt.xlabel('Number of Randomly Rotated Cubes')
plt.ylabel('Shadow Area [units$^2$]')
plt.legend()
plt.show()
