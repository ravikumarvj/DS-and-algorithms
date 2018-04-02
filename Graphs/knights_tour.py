from digraph import DiGraph
from queue import LifoQueue

def is_valid_move(x, y, row, column):
    return 0 <= x < row and 0 <= y < column


def find_neigh(i, j, row, column):
    moves = ((-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1))
    ret = []
    for x, y in moves:
        pos1, pos2 = i + x, j + y
        if is_valid_move(pos1, pos2, row, column):
            ret.append(pos1 * row + pos2)

    return ret


def make_graph(row, column):
    graph = DiGraph()

    for i in range(row):
        for j in range(column):
            key = i * row + j
            neigh_list = find_neigh(i, j, row, column)

            for neigh in neigh_list:
                graph.add_edge(key, neigh)

    return graph


def order_by_avail(graph, pos, visited):
    ret = []
    for neigh in graph.vert_list[pos].get_neighs():
        if neigh not in visited:
            c = 0
            for i in graph.vert_list[neigh].get_neighs():
                if i not in visited:
                    c += 1

            ret.append((neigh, c))

    # wrong because ret.sort return None
    # l = [y[0] for y in ret.sort(key=lambda x:x[1])]
    l = [y[0] for y in sorted(ret, key=lambda x:x[1])]
    return l


def print_tour_rec(graph, pos, path, visited):
    visited.add(pos)
    path.append(pos)

    if len(path) == graph.num_vert:
        return True

    for neigh in order_by_avail(graph, pos, visited):
        if (neigh not in visited) and print_tour_rec(graph, neigh, path, visited):
            return True
    visited.remove(pos)
    path.pop()
    return False


def print_tour(graph, start_pos):
    path = []
    visited = set()

    print_tour_rec(graph, start_pos, path, visited)
    return path


if __name__ == '__main__':
    graph = make_graph(30, 30)

    # for v in graph:
    #    print(v)

    print(graph.num_vert)

    from time import time
    print(time())
    l = print_tour(graph, 6)
    print(l)
    print(time())
