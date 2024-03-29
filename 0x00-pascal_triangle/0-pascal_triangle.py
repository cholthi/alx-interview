#!/usr/bin/python3
"""
function to generate n rows of pascal's triangle"""


def pascal_triangle(n):
    """ Returns `n` of the pascal's triangle"""
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    prevRows = pascal_triangle(n - 1)
    newRow = [1] * n
    for i in range(1, n - 1):
        newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
    prevRows.append(newRow)
    return prevRows
