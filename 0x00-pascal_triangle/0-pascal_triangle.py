#!/usr/bin/python3

def pascal_triangle(n):
    matrix = [[1]]
    if (n == 1):
        return matrix
    for i in range(1, n):
        temp = [0] + matrix[-1] + [0]
        row = []
        for j in range(len(matrix[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        matrix.append(row)
    return matrix
