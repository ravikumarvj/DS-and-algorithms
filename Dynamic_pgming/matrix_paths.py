### COPIED ### VERIFIED
"""
Given N x M matrix, write a function to count the number of ways of starting at the top-left corner
and getting to the bottom-right corner. You can only move right or down.
For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""


def find_paths(row, colomn):

    # matrix is used for memoization
    matrix = [[0 for _ in range(colomn)] for _ in range(row)]

    # There is only one path to reach any of matrix[i][0]
    for i in range(row):
        matrix[i][0] = 1
    # similarly only one path to reach any of matrix[0][j]
    for j in range(colomn):
        matrix[0][j] = 1

    for i in range(1, row):
        for j in range(1, colomn):
            # to reach (i, j) we can come only through (i-1, j) or (i, j-1)
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[row-1][colomn-1]


print(find_paths(3, 2))
