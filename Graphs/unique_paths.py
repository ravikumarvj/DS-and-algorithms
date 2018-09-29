### COPIED ###
from queue import Queue
from digraph import DiGraph
from graph import NGraph


def count_paths_r(g, start, end, path, visited):
    if start == end:
        print(path)
        return 1

    count = 0
    for neigh in g.vert_list[start].get_neighs():
        if neigh not in visited:
            path.append(neigh)
            visited.add(neigh)
            count += count_paths_r(g, neigh, end, path, visited)

            path.pop()
            visited.remove(neigh)
    return count


def count_paths(g, start, end):  # No loops in path
    path = [start]
    visited = set()
    visited.add(start)
    return count_paths_r(g, start, end, path, visited)


def _paths_with_m_edges(g, start, end, m, path, visited):  # COPIED
    if m == 0:   # Do not proceed to any more nodes if m becomes 0
        if start == end:  # found a path.
            print(path)
            return 1  # return 1 as found a path.
        else:  # Not a path to destination. Return without printing
            return 0  # Not a path return 0
    else:
        count = 0
        node = g.vert_list[start]

        for neigh in node.get_neighs():
            if neigh not in visited:
                path.append(neigh)
                visited.add(neigh)
                # Go through all neighbours and find path. Each neighbour may return counts >= 0
                count += _paths_with_m_edges(g, neigh, end, m-1, path, visited)

                visited.remove(neigh)
                path.pop()
    return count  # return count. not 1


def paths_with_m_edges(g, start, end, m):  # COPIED
    # uses DFS. Counts as well as prints all the paths
    path = [start]
    visited = set()
    visited.add(start)
    return _paths_with_m_edges(g, start, end, m, path, visited)

def paths_with_m_edges_bfs(g, start, end, m):   # COPIED
    # uses BFS. (For printing path, DFS is better). Here, we dont handle cycles well
    visited = set()  # No use of visited. Use 'm' as stopping point instead
    q = Queue()
    q.put((start, m))

    count = 0
    while not q.empty():
        start, m = q.get()
        if m == 0:
            if start == end:
                count += 1
        else:
            node = g.vert_list[start]
            for neigh in node.get_neighs():
                q.put((neigh, m-1))
    return count


def _maximum_cost_path(g, start, end, visited, path, cost):  # COPIED
    # cost in the parametes is the cost seen so far down the path.
    if start == end:
        # We need to print the max cost path.
        # To return the same in the outer function, we should return it along with the cost.
        # Outer function can compare costs returned from various recursive calls and choose the
        # maximum cost and corresponding path accordingly.
        return cost, path

    maxim = 0
    maxim_path = []

    node = g.vert_list[start]
    for neigh in node.get_neighs():
        if neigh not in visited:
            path.append(neigh)
            visited.add(neigh)
            ret, m_path = _maximum_cost_path(g, neigh, end, visited, path, cost + node.get_weight(neigh))
            maxim = max(ret, maxim)
            if ret == maxim:  # this is the maximum seen so far.
                maxim_path = m_path.copy()  # NBNBNBNB: Do a copy().
            path.pop()
            visited.remove(neigh)
    return maxim, maxim_path  # If not connected, return (0, [])


def maximum_cost_path(g, start, end):  # COPIED
    visited = set()
    visited.add(start)
    path = [start]
    return _maximum_cost_path(g, start, end, visited, path, 0)

if __name__ == '__main__':
    g = DiGraph()
    g.add_edge(0, 1)
    g.add_edge(0, 6)
    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(1, 6)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(5, 2)
    g.add_edge(5, 3)
    g.add_edge(5, 4)
    g.add_edge(6, 5)
    g.add_edge(7, 1)
    g.add_edge(7, 6)
    print(count_paths(g, 1, 5))
    print(paths_with_m_edges(g, 0, 3, 4))
    print('***')
    g = NGraph()
    g.add_edge(0, 1, 5)
    g.add_edge(0, 6, 11)
    g.add_edge(1, 2, 7)
    g.add_edge(1, 5, 5)
    g.add_edge(1, 6, 3)
    g.add_edge(1, 7, 6)
    g.add_edge(2, 3, -8)
    g.add_edge(2, 5, -1)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 9)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 9)

    print(maximum_cost_path(g, 0, 7))