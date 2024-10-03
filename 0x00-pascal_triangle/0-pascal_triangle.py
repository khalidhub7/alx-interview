#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        if i == 0:
            pascal.append([1])
            continue
        row = [1]
        for j in range(1, i):
            row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        row.append(1)
        pascal.append(row)
    return pascal
