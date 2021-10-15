import numpy as np
from data_gen import N
from Point import Point

points = [0] * N  # массив точек

for i in range(N):
    points[i] = Point(i)

n = 50  # число итераций
for i in range(n):
    u = [point.u for point in points]
    for point in points:
        if point.u != 1 and point.u != -1:
            for j in range(point.bounds):
                point.u -= point.alpha[j + 1] * u[point.neighbours[j][1]] / point.alpha[0]

e = np.zeros((N, 2))
e[:, 0] = u
e[:, 1] = u
print(e)