#!/usr/bin/python3
"""Module that defines a function to rotate a 2D matrix in-place."""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): a list of lists representing the n x n matrix.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
