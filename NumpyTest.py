import numpy as np
import itertools
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

def metrics():
    numPoints = 50
    mean = np.array([0,0,0])
    cov = np.array([[1,0,0],[0,1,0],[0,0,1]])
    points = np.random.multivariate_normal(mean, cov, numPoints) # mvnrnd

    print(points[:,0])

    euclidian = np.linalg.norm(points)

    print(euclidian)

    fig = pyplot.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(points[:,0], points[:,1], points[:,2], marker='o', color='blue', s=40, label='point')

    i = 1
    arrayPoints = []
    while (i <= numPoints):
        arrayPoints.append(i)
        i = i + 1
    combos = list(itertools.combinations(arrayPoints, 2))

    combos = [list(item) for item in combos]

    pyplot.show()

if __name__ == '__main__':
    metrics()
