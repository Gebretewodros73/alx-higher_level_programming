#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sque_mat = matrix
    new_matrix = sque_mat
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sque_mat[i][j] = new_matrix[i][j] ** 2
    return sque_mat
