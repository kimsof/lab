import numpy as np
from data_gen import data


class Point:

    def __init__(self, number):
        self.number = number                     # номер точки
        self.x = np.round(data[number, 0], 3)    # х
        self.y = np.round(data[number, 1], 3)    # у
        self.bounds = data[number, 2]            # число соседей
        self.neighbours = data[number, 3]        # соседи
        self.u = data[number, 4]                 # значение функции u

    # заполнение матрицы системы А для каждой точки, не являющейся стоком/источником
        if self.u == 0:
            dxdy = np.zeros((len(self.neighbours), 2))
            for i in range(len(self.neighbours)):
                dxdy[i, 0] = data[self.neighbours[i], 0] - self.x
                dxdy[i, 1] = data[self.neighbours[i], 1] - self.y
            A = np.zeros((len(self.neighbours) + 1, len(self.neighbours) + 1))
            A[0, :] = np.ones(len(self.neighbours) + 1)
            A[1, 1:] = dxdy[:, 0]
            A[2, 1:] = dxdy[:, 1]
            A[3, 1:] = dxdy[:, 0] ** 2
            A[4, 1:] = dxdy[:, 1] ** 2

            if len(self.neighbours) == 4:
                b = np.array([0, 0, 0, 2, 2])

            if len(self.neighbours) == 5:
                A[5, 1:] = dxdy[:, 0] * dxdy[:, 1]
                b = np.array([0, 0, 0, 2, 2, 0])

            if len(self.neighbours) == 6:
                A[5, 1:] = dxdy[:, 0] * dxdy[:, 1]
                A[6, 1:] = dxdy[:, 0] ** 3
                b = np.array([0, 0, 0, 2, 2, 0, 0])

            if len(self.neighbours) == 7:
                A[5, 1:] = dxdy[:, 0] * dxdy[:, 1]
                A[6, 1:] = dxdy[:, 0] ** 3
                A[7, 1:] = dxdy[:, 0] ** 2 * dxdy[:, 1]
                b = np.array([0, 0, 0, 2, 2, 0, 0, 0])

            if len(self.neighbours) == 8:
                A[5, 1:] = dxdy[:, 0] * dxdy[:, 1]
                A[6, 1:] = dxdy[:, 0] ** 3
                A[7, 1:] = dxdy[:, 0] ** 2 * dxdy[:, 1]
                A[8, 1:] = dxdy[:, 0] * dxdy[:, 1] ** 2
                b = np.array([0, 0, 0, 2, 2, 0, 0, 0, 0])

            if len(self.neighbours) == 9:
                A[5, 1:] = dxdy[:, 0] * dxdy[:, 1]
                A[6, 1:] = dxdy[:, 0] ** 3
                A[7, 1:] = dxdy[:, 0] ** 2 * dxdy[:, 1]
                A[8, 1:] = dxdy[:, 0] * dxdy[:, 1] ** 2
                A[9, 1:] = dxdy[:, 1] ** 3
                b = np.array([0, 0, 0, 2, 2, 0, 0, 0, 0, 0])

            if len(self.neighbours) == 10:
                A[5, 1:] = dxdy[:, 0] * dxdy[:, 1]
                A[6, 1:] = dxdy[:, 0] ** 3
                A[7, 1:] = dxdy[:, 0] ** 2 * dxdy[:, 1]
                A[8, 1:] = dxdy[:, 0] * dxdy[:, 1] ** 2
                A[9, 1:] = dxdy[:, 1] ** 3
                A[10, 1:] = dxdy[:, 0] ** 4
                b = np.array([0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0])

            self.alpha = np.linalg.solve(A, b)  # коэффициенты разложения лапласиана

# функция, возвращающаяя расстояние между двумя точками
    def distance(self, other):
        if isinstance(other, int):
            return ((self.x - data[other, 0]) ** 2 + (self.y - data[other, 1]) ** 2) ** (1 / 2)
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2)

# функция для вывода информации о точке через интерфейс
    def inp(self):
        data_neighbours = ''
        for i in range(self.bounds):
            m = self.neighbours[i]
            data_neighbours += f'\n{(m, np.round(data[m, 0], 3), np.round(data[m, 1], 3), np.round(((self.x - data[m, 0]) ** 2 + (self.y - data[m, 1]) ** 2) ** (1 / 2), 3))}'
        return [self.number, (self.x, self.y), data_neighbours, self.u]
