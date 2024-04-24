#!/usr/bin/python3
"""
Provides function to rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """ Roate 2d matrix
    """
    no_rows = len(matrix)
    for i in range(no_rows):
        for j in range(i, no_rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(no_rows):
        matrix[i] = matrix[i][::-1]
