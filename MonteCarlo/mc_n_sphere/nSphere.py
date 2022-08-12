import numpy as np

def integrate(npoints, dim, radius):
    '''
    Returns the volume of an n-sphere (i.e. a sphere in
    n+1 dimensional space) of a given radius using 
    multidimensional Monte Carlo integration.
    '''
    # the random points in our hypercube
    rs = np.random.uniform(-radius, radius, size=(npoints,dim))

    counter = 0
    for r in rs:
        d = 0 # distance from centre of hypercube
        for r_i in r:
            d += r_i**2
        if d < radius:
            counter += 1
            
    volume = ((2*radius)**dim) * counter / npoints

    return volume

if __name__ == "__main__":

    print("Enter the number of points to use for MC Integration (a big number)")
    npoints = int(input())

    print("Enter the dimensionality of the space you're in")
    dim = int(input())

    print("Enter the radius of your sphere")
    radius = float(input())

    print(integrate(npoints, dim, radius))