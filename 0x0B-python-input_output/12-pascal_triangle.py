#!/usr/bin/python3
"""
Defines pasacal triangle that create list of lists
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle
    """

    # return an empty list if n <= 0
    if n <= 0:
        return []

    # create an empty list to hold the Pascal's triangle
    pascal = []

    # loop through the number of rows in the Pascal's triangle
    for i in range(n):
        # create an empty list to hold the values for this row
        row = []
        # loop through each column in the row
        for j in range(i + 1):
            # if it's the first or last column, set the value to 1
            if j == 0 or j == i:
                row.append(1)
            # otherwise, calculate the value based on the previous row
            else:
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        # add the row to the Pascal's triangle
        pascal.append(row)

    # return the Pascal's triangle
    return pascal
