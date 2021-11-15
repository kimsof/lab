import numpy as np
from data_gen import N
from Point import Point

points = [Point(k) for k in range(N)]  # массив точек

I = 50  # число итераций
for i in range(I):
    u = [point.u for point in points]
    for point in points:
        if point.u != 1 and point.u != -1:
            point.u = -np.dot(point.alpha[1:], [u[neib[0]] for neib in point.neighbours])/point.alpha[0]

for i in range(N):
    print(i, u[i])