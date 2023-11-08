import numpy as np

# функция возвращает матрицу расстояний между векторами
def compute_distance(x):
    matrix = []
    for i in range(len(x)):
        matrix.append([])
        for j in range(len(x)):
            if i == j:
                matrix[i].append(0)
            else:
                matrix[i].append(sum((np.array(x[i]) - np.array(x[j])) ** 2))
    return matrix