import numpy as np

np.random.seed(100)

N = 100  # np.random.randint(100, 201)          # число точек
data = np.zeros((N, 6), dtype=object)  # массив со всей информацией
data[:, :2] = np.random.random_sample((N, 2))  # x и y каждой точки
data[:, 2] = np.random.randint(-1, 2, N)  # источник/сток/ничего
data[:, 3] = np.random.randint(4, 11, N)  # число связей (соседей) каждой точки

array = np.array([[-1, 1], [0, 1], [1, 1],
                  [-1, 0], [0, 0], [1, 0],
                  [-1, -1], [0, -1], [1, -1]])


# функция, рандомно генерирующая соседей для каждой точки
def get_neighbours():
    bonds = np.zeros(N, dtype=object)
    bonds += data[:, 3]
    if sum(bonds) % 2 != 0:
        bonds[list(bonds).index(max(bonds))] -= 1

    bonds_dictionary = {}
    for i in range(N):
        bonds_dictionary[i] = bonds[i]

    dictionary_items = list(bonds_dictionary.items())
    dictionary_items.sort(key=lambda i: i[1])
    dictionary_items = dictionary_items[::-1]

    keys = []
    neighbours_total = []
    for i in range(N):
        keys.append(dictionary_items[i][0])
        neighbours_total.append([])

    while len(keys) > 0:
        n = keys[0]
        del keys[0]
        x_n = data[n, 0]
        y_n = data[n, 1]
        distances = np.zeros(N, dtype=object)

        for i in range(N):
            distance_variants = np.zeros(9)
            for j in range(9):
                distance_variants[j] = ((x_n - (data[i, 0] + array[j][0])) ** 2 + (
                        y_n - (data[i, 1] + array[j][1])) ** 2) ** (1 / 2)
            distances[i] = [np.argmin(distance_variants), distance_variants[np.argmin(distance_variants)]]

        radius = 0
        points_in_radius = []
        while len(points_in_radius) < bonds[n]:
            for i in range(N):
                if distances[i][1] < radius and i != n and not i in [neib[1] for neib in neighbours_total[
                    n]] and not i in points_in_radius and i in keys:
                    points_in_radius.append(i)
            radius += 0.01
            if radius > 2 ** (1 / 2):
                raise OverflowError

        neighbours = np.random.choice(points_in_radius, int(bonds[n]), False)
        neighbours_total[n] += [[array[distances[neib][0]], neib] for neib in neighbours]

        for neib in neighbours:
            neighbours_total[neib].append([array[distances[neib][0]] * -1, n])
            bonds[neib] -= 1
            if bonds[neib] == 0:
                del keys[keys.index(neib)]

    return neighbours_total


# не всегда функции get_neighbours() удается распределить соседей корректно для всех точек c 1 раза, поэтому:
for i in range(10):
    try:
        neighbours = get_neighbours()
        break
    except OverflowError:
        continue

for i in range(N):
    data[i, 4] = neighbours[i]

print(N)
