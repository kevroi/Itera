import random
import numpy as np
import cv2

def eucDist(x,y,r):
    '''
    Calculates Euclidean Distance between the point (x,y) and the position
    vector r 
    '''
    return np.sqrt((x-r[0])**2+(y-r[1])**2)

def manDist(x,y,r):
    return abs(x-r[0])+abs(y-r[1])

def makePallette(N):
    return {i:[random.randint(0,255) for c in range(3)] for i in range(N)}

def uniformPoints(r,N):
    '''
    Returns N uniformly distributed (x,y) coordinates on an r by r plane
    '''
    return [(random.randint(0,r+1), random.randint(0,r+1)) for _ in range(N)]

def gaussPoints(r,N):
    '''
    IN PROGRESS
    Returns N (x,y) coordinates on an r by r plane, normally distributed 
    about the centre.
    Each point has a 0.3% chance of not being in the plane :(
    '''
    points = [np.round(np.random.normal(scale=r, size=2)) for _ in range(N)]
    # Centre coordinates about centre of plane
    points = [i + np.array((r//2, r//2)) for i in points]
    points = np.abs(points)
    points = [point.tolist() for point in points]
    return points



def voronify(r, N, metric):
    # INITIALISATION
    if metric == 'e':
        dist = eucDist

    elif metric == 'm':
        dist = manDist

    else:
        dist = eucDist


    # array to store nearest distance values
    canvas = np.full((r,r), np.inf)
    # array to temporarily remember distances from a given point during iteration
    dist_canvas = np.zeros((r,r))
    # array to remmeber which pixel belongs to which Voronoi cell
    index_canvas = np.full((r,r), np.inf)

    # Generate centres for each Voronoi Cell
    points = uniformPoints(r,N)
    # points = gaussPoints(r/3, N) # 99.7% of points will lie within 3 stddev of mean

    for point in points:
        for i in range(canvas.shape[0]):
            for j in range(canvas.shape[1]):
                dist_canvas[i][j] = dist(i, j, point)
                if dist_canvas[i][j] < canvas[i][j]:
                    canvas[i][j] = dist_canvas[i][j]
                    index_canvas[i][j] = points.index(point)

    image = np.zeros((r,r,3), np.uint8)
    pallette = makePallette(N)
    for i in range(r):
        for j in range(r):
            image[i][j] = pallette[index_canvas[i][j]]

    # Display Image
    cv2.imshow('Voronoi Diagram',image)
    # Press any button to close
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        

if __name__ == "__main__":

    print("Enter number of pixels for an edge of the square plane")
    r = int(input())

    print("Enter number of shards you want (i.e. Voronoi Cells)")
    N = int(input())

    print("Enter 'e' for Euclidean Distances or 'm for Manhattan Distances")
    metric = str(input())

    voronify(r,N,metric)