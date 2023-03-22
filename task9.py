import numpy as np
from functools import partial
from format_table import format_table
import time
from collections import namedtuple

matrix_extend = partial(np.pad, pad_width=(1, 0), constant_values=0)


def matrices_mult(matrix1, matrix2):

    dim = np.shape(matrix1)[0]
    new_matrix = np.zeros(shape=(dim, dim))

    for i in range(dim):
        for j in range(dim):
            for k in range(np.shape(matrix2)[0]):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return new_matrix


def recursive_matrix_mult(matrix1, matrix2):

    old_dim = np.shape(matrix1)[0]
    dim = old_dim
    if old_dim == 1:
        return matrix1 * matrix2

    if old_dim % 2 == 1:
        matrix1, matrix2 = map(matrix_extend, [matrix1, matrix2])
        dim += 1

    new_dim = dim // 2

    a = matrix1[:new_dim, :new_dim]
    b = matrix1[:new_dim, new_dim:]
    c = matrix1[new_dim:, :new_dim]
    d = matrix1[new_dim:, new_dim:]
    e = matrix2[:new_dim, :new_dim]
    f = matrix2[:new_dim, new_dim:]
    g = matrix2[new_dim:, :new_dim]
    h = matrix2[new_dim:, new_dim:]

    q1 = recursive_matrix_mult(a, e) + recursive_matrix_mult(b, g)
    q2 = recursive_matrix_mult(a, f) + recursive_matrix_mult(b, h)
    q3 = recursive_matrix_mult(c, e) + recursive_matrix_mult(d, g)
    q4 = recursive_matrix_mult(c, f) + recursive_matrix_mult(d, h)

    new_matrix = np.bmat([[q1, q2], [q3, q4]])

    if old_dim != dim:
        new_matrix = new_matrix[1:, 1:]

    return np.matrix(new_matrix)


def strassen_algorithm(matrix1, matrix2):

    old_dim = np.shape(matrix1)[0]
    dim = old_dim
    if old_dim == 1:
        return matrix1 * matrix2

    if old_dim % 2 == 1:
        matrix1, matrix2 = map(matrix_extend, [matrix1, matrix2])
        dim += 1

    new_dim = dim // 2

    a = matrix1[:new_dim, :new_dim]
    b = matrix1[:new_dim, new_dim:]
    c = matrix1[new_dim:, :new_dim]
    d = matrix1[new_dim:, new_dim:]
    e = matrix2[:new_dim, :new_dim]
    f = matrix2[:new_dim, new_dim:]
    g = matrix2[new_dim:, :new_dim]
    h = matrix2[new_dim:, new_dim:]

    p1 = strassen_algorithm(a, f - h)
    p2 = strassen_algorithm(a + b, h)
    p3 = strassen_algorithm(c + d, e)
    p4 = strassen_algorithm(d, g - e)
    p5 = strassen_algorithm(a + d, e + h)
    p6 = strassen_algorithm(b - d, g + h)
    p7 = strassen_algorithm(a - c, e + f)

    q1 = p5 + p4 - p2 + p6
    q2 = p1 + p2
    q3 = p3 + p4
    q4 = p1 + p5 - p3 - p7

    new_matrix = np.bmat([[q1, q2], [q3, q4]])

    if old_dim != dim:
        new_matrix = new_matrix[1:, 1:]

    return np.matrix(new_matrix)


def matrix_equal(matrix1, matrix2):

    dim = np.shape(matrix1)[0]

    for i in range(dim):
        for j in range(dim):
            if matrix1[i, j] != matrix2[i, j]:
                return False
    return True


def fill_matrix_random(matrix):
    dim = np.shape(matrix)[0]
    for x in range(dim):
        for y in range(dim):
            matrix[x, y] = np.random.randint(0, 200)
    pass


def matrix_generate(dim):
    m1 = np.zeros((dim, dim))
    m2 = np.zeros((dim, dim))
    fill_matrix_random(m1)
    fill_matrix_random(m2)
    return m1, m2





def mult(array):
    res = 1
    for el in array:
        if el != 0:
            res *= el
    return res


def stat_count(results):
    geometric_mean = mult(results) ** (1 / len(results))
    mean = sum(results) / len(results)
    std_deviation = np.sqrt(sum(list(map(lambda x: (mean - x) ** 2, results))) / len(results))
    res = namedtuple("Stat", ["geometric_mean", "mean", "std_deviation"])
    res.geometric_mean = geometric_mean
    res.mean = mean
    res.std_deviation = std_deviation
    return res


TEST_COUNT = 1


def timer(funcs, test_data):
    results = {}
    for func in funcs:
        for data in test_data:
            stopwatch = []
            for i in range(TEST_COUNT):
                start = time.time()
                func(*data)
                end = time.time()
                stopwatch.append(end - start)
            stats = stat_count(stopwatch)
            stats = f"gm: {stats.geometric_mean} mn: {stats.mean}, dev: {stats.std_deviation}"
            if func.__name__ in results.keys():
                results[func.__name__][str(np.shape(data[0]))] = stats
            else:
                results[func.__name__] = {}
                results[func.__name__][str(np.shape(data[0]))] = stats
    return results


data = []

data.append(list(matrix_generate(1024)))
# for i in range(800, 1000, 50):
#     data.append(list(matrix_generate(i)))


res = timer([strassen_algorithm], data)
algos = list(res.keys())
benchmarks = list(res["strassen_algorithm"].keys())
results = []

for benchmark in benchmarks:
    tmp = []
    for alg in algos:
        tmp.append(res[alg][benchmark])
    results.append(tmp)


print(res)

format_table(benchmarks, algos, results)
