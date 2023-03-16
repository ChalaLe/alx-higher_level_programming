#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = matrix.copy()

    for i in range(len(matrix)):
        result[i] = list(map(lambda x: x**2, matrix[i]))

    return (result)
