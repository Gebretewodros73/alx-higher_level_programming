#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
try:
    matrix = [4, 5, 6]
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)
try:
    matrix = [
            ['t', 2, 3],
            [4, 5, 6]
            ]
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)
try:
    matrix = [
            [1, 2, 3],
            [4, 5]
            ]
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)
try:
    matrix = [
            [1, 2, 3],
            [4, 5, 6]
            ]
    print(matrix_divided(matrix, 't'))
    print(matrix)
except Exception as e:
    print(e)
try:
    matrix = [
            [1, 2, 3],
            [4, 5, 6]
            ]
    print(matrix_divided(matrix, 0))
    print(matrix)
except Exception as e:
    print(e)

