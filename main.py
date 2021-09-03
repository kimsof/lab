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
            value = 0
            for j in range(0, len(point.neighbours)):
                value += point.alpha[j + 1] * u[point.neighbours[j]] / point.alpha[0]
            point.u = value


#     w = [point.u for point in points]
#
# e = np.zeros((N, 2))
# e[:, 0] = u
# e[:, 1] = w


