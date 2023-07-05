#!/usr/bin/python3
"""dividing matrics by a certian number"""


def matrix_divided(matrix, div):
    """function"""
    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, (int, float)) for row in matrix for ele in row)):
        raise TypeError("matrix must contain only integers or floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
