import numpy as np
from functools import partial

matrix_extend = partial(np.pad, pad_width=(1, 0), constant_values=0)


def matrices_mult(matrix1, matrix2):

    dim = np.shape(matrix1)[0]
    new_matrix = np.zeros(dim)

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


for i1 in range(20):
    m1 = [[np.random.randint(0, 200) for i in range(20)] for j in range(20)]
    m2 = [[np.random.randint(0, 200) for k in range(20)] for t in range(20)]
    m1, m2 = map(np.matrix, [m1, m2])
    assert matrix_equal(np.dot(m1, m2), strassen_algorithm(m1, m2))

