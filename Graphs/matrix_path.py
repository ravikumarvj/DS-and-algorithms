#### COPIED #### VERIFIED
"""
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
required to reach the end coordinate from the start. If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls.
You cannot wrap around the edges of the board.

For example, given the following board:
[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left),
the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2)
because there is a wall everywhere else on the second row.
"""
from queue import Queue


def get_neighs(node, row_len, colon_len, matrix):
    steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    neighs = []
    for step in steps:
        row = step[0] + node[0]
        colon = step[1] + node[1]
        if 0 <= row < row_len and 0 <= colon < colon_len and matrix[row][colon] is False:
            neighs.append((row, colon))

    return neighs


def print_steps(start, stop, matrix):
    q = Queue()
    visited = [[0 for i in range(len(matrix[0]))] for j in matrix]
    q.put((start, 0))
    visited[start[0]][start[1]] = True

    while not q.empty():
        node, step = q.get()
        if node == stop:
            return step

        neighs = get_neighs(node, len(matrix), len(matrix[0]), matrix)
        for neig in neighs:
            if not visited[neig[0]][neig[1]]:
                q.put((neig, step + 1))
                visited[neig[0]][neig[1]] = True

    return None


if __name__ == '__main__':
    t = True
    f = False
    matrix = [[t, t, t, t, t, f, f], [t, t, t, f, f, f, f], [t, t, f, f, t, t, f], [t, f, t, t, t, t, f],
              [t, f, f, t, t, f, f,], [t, t, f, t, f, f, t], [t, t, f, f, f, t, t]]

    start = (0, 6)
    stop = (4, 2)
    print(print_steps(start, stop, matrix))