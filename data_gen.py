import numpy as np

N = np.random.randint(100, 201)  # число точек
data = np.zeros((N, 5), dtype=object)  # массив со всей информацией
data[:, :2] = np.random.random_sample((N, 2))  # x и y каждой точки
data[:, 2] = np.random.randint(4, 11, N)  # число связей (соседей) каждой точки
data[:, 4] = np.random.randint(-1, 2, N)  # источник/сток/ничего

# функция, рандомно генерирующая соседей для каждой точки
def get_neighbours():
    bonds = np.zeros(N, dtype=object)
    bonds += data[:, 2]
    if sum(bonds) % 2 != 0:
        bonds[list(bonds).index(max(bonds))] -= 1

    dictionary = {}
    for i in range(N):
        dictionary[i] = bonds[i]

    dictionary_items = list(dictionary.items())
    dictionary_items.sort(key=lambda i: i[1])
    dictionary_items = dictionary_items[::-1]

    keys = []
    all_neighbours = []
    for i in range(N):
        keys.append(dictionary_items[i][0])
        all_neighbours.append([])

    while len(keys) > 0:
        n = keys[0]
        del keys[0]
        neighbours = list(np.random.choice(keys, int(bonds[n]), False))
        all_neighbours[n] += neighbours

        for neib in neighbours:
            all_neighbours[neib].append(n)
            bonds[neib] -= 1
            if bonds[neib] == 0:
                del keys[keys.index(neib)]

    return all_neighbours

# невсегда функции get_neighbours() удается распределить соседей корректно для всех точек, поэтому:
for i in range(10):
    try:
        neighbours = get_neighbours()
        break
    except ValueError:
        continue


for i in range(N):
    data[i, 3] = sorted(neighbours[i])

print(N)