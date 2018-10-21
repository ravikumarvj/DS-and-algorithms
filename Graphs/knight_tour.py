### COPIED ###  VERIFIED
from digraph import DiGraph
from queue import Queue

class KnightsTour:
    def __init__(self, row, column):
        self.board = DiGraph()  # Directed graph
        self.row = row
        self.column = column

        for r in range(row):
            for c in range(column):
                pos = (r * column) + c
                # For each position, find the valid moves and add as edges
                for neigh in self.get_neighs(r, c):
                    self.board.add_edge(pos, neigh)

    def get_neighs(self, row, column):
        # For each position, there can be up to 8 valid moves
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]
        ret = []

        for x, y in moves:
            n_row = row + x
            n_clm = column + y
            # If a valid move, add it to return list
            if 0 <= n_row < self.row and 0 <= n_clm < self.column:
                neigh = n_row * self.column + n_clm
                ret.append(neigh)

        return ret

    def order_by_avail(self, start, visited):
        ret = []

        node = self.board.vert_list[start]
        for neigh in node.get_neighs():
            if neigh in visited:
                continue
            c = 0
            for next in self.board.vert_list[neigh].get_neighs():
                if next not in visited:
                    c += 1
            #  Out of for loop. C can be 0 also. Still need to include in ret
            ret.append((neigh, c))

        # wrong because ret.sort return None
        # return [y[0] for y in ret.sort(key=lambda x:x[1])]
        return [y[0] for y in sorted(ret, key=lambda x:x[1])]

    def solve(self, start):
        visited = set()
        path = []  # passing of path technique happens with DFS
        return self._solve(start, path, visited)

    def _solve(self, start, path, visited):
        path.append(start)
        visited.add(start)  # mark this node as visited
        if len(visited) == self.board.num_vert:  # Visited all nodes
            print(path)
            return 1

        count = 0
        # for neigh in node.get_neighs():
        for neigh in self.order_by_avail(start, visited):
            if neigh in visited:  # neigh may get visited after getting it as list in order_by_avail
                continue
            count += self._solve(neigh, path, visited)
            # if self._solve(neigh, path, visited): # solve using neigh
                # If solved, Done
            #     return True

        # Done with start. No path found through it.
        visited.remove(start)
        path.pop()
        return count


# Given a location, find its unvisited neighbours as a list
def get_neighs(number, row, colom, visited):
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]
    c = number % colom
    r = number//colom

    ret = []

    for move in moves:
        n_r = r + move[0]
        n_c = c + move[1]

        if 0 <= n_r < row and 0 <= n_c < colom:
            pos = n_r*colom + n_c

            if pos not in visited:  # Only add unvisited
                ret.append(pos)
    return ret


# Print path, backwards (Keep a list and reverse it, if fwd is needed)
def print_path(path, start, end):
    temp = end
    while temp is not None:
        print(temp, end=' ')
        temp = path[temp]
    print()


def minimum_moves(start, end, row, colom):  # start = source, end = destination
    if start == end:
        return 0

    path = dict()  # Used to print path
    visited = set()  # visited for BFS
    q = Queue()  # Queue for BFS
    q.put((start, 0))  # Put start. 0 is the distance
    visited.add(start)  # start is now visited.
    path[start] = None  # start is the starting node of path

    while not q.empty():
        temp, moves = q.get()
        for neigh in get_neighs(temp, row, colom, visited):
            if neigh == end:  # Before putting queue, check if end.
                path[end] = temp  # path to end is through temp
                print_path(path, start, end)
                return moves + 1  # +1 as it is neigh
            if neigh not in visited:
                q.put((neigh, moves + 1))
                visited.add(neigh)  # visit when adding to q
                path[neigh] = temp

    return -1


if __name__ == '__main__':
    board = KnightsTour(8, 8)
    start = 3
    from time import time
    # t = time()
    count = 0
    for start in range(64):
        count += board.solve(start)
    # print(time()-t)
    print(count)
    # print(minimum_moves(35, 36, 8, 8))