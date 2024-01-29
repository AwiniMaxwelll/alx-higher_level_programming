#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    It computes and returns the square of each element a matrix.
    The function does not modify the original matrix.
    """
    new_matrix = []
    for matrix1 in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, matrix1)))
    return new_matrix
