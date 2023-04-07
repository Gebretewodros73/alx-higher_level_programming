#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix (lists): A list of integer or float
        div (int or float): The number to divide

    Returns:
        new matrix

    Raises:
        TypeError: If 'matrix' is not a list of lists
        of Integers/floats or if 'div' is not a number.
               If each row of 'matrix' is not the same size.
        ZeroDivisionError: If 'div' is equal to 0.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 \
            or not all(isinstance(row, list) for row in matrix) or \
            not all(all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by Zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
