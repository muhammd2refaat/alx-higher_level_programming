#!/usr/bin/python3
"""
Technical interview preparation:
You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.
    Each row represents the coefficients of the binomial expansion
    in a triangular arrangement. Rows are encoded as lists of integers.
    """
    if n <= 0:
        return []

    result = [[1]]
    for current_row in range(1, n):
        row_data = [1]
        for element_index in range(1, current_row):
            row_data.append(
                result[current_row-1][element_index-1]
                + result[current_row-1][element_index])
        row_data.append(1)
        result.append(row_data)

    return result
