#!/usr/bin/python3
"""This module is for matrix_divided method"""


def matrix_divided(matrix, div):
    """This divides elements of a matrix.

    Arguments:
        matrix: The matrix whose elements are to be divided by divided.
        div: This is the dividing number.

    Raises:
        TypeError: If the matrix is not a lists of int or float.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If the div is neither an int nor float
        ZeroDivisionError: If the div is zero

    Returns:
        a new matrix with elements rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
