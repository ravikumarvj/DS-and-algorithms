### COPIED ###  VERIFIED

from graph import NGraph


def print_all_hamilton_path_r(g, start, path, visited):
    # All nodes are visited. Found a hamilton path.
    if len(visited) == len(g.vert_list):
        print(path)
        return

    node = g.vert_list[start]
    for neigh in node.get_neighs():
        if neigh not in visited:  # Go through the unvisited nodes to find a path
            path.append(neigh)
            visited.add(neigh)

            print_all_hamilton_path_r(g, neigh, path, visited)

            path.pop()
            # Done with neigh, free it so that it can be part of another path
            visited.remove(neigh)


def print_all_hamilton_path(g, start):
    path = [start]
    visited = set()
    visited.add(start)  # ADD start to visited here
    # Find all paths starting from 'start' node and see if all nodes are visited
    print_all_hamilton_path_r(g, start, path, visited)


def print_all_hamilton_cycles_r(g, start, end, path, visited):
    visited.add(start)
    path.append(start)

    if start == end:
        # print path, only if we reach back 'start' after visiting all nodes
        if len(visited) == len(g.vert_list):
            print(path)
        path.pop()  # pop the node before return
        visited.remove(start)
        return

    node = g.vert_list[start]
    for neigh in node.get_neighs():
        if neigh not in visited:
            print_all_hamilton_cycles_r(g, neigh, end, path, visited)

    path.pop()
    visited.remove(start)


def print_all_hamilton_cycles(g, start):
    path = []
    visited = set()
    path.append(start) # start will be there is path twice (start and end)
    # start is not visited yet

    node = g.vert_list[start]
    # Go through all the neighbours of start and find a path ending at start
    for neigh in node.get_neighs():
        print_all_hamilton_cycles_r(g, neigh, start, path, visited)

if __name__ == '__main__':
    g = NGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 7)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    g.add_edge(4, 6)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    # g.add_edge(6, 8)
    print_all_hamilton_path(g, 5)
    print('****')
    print_all_hamilton_cycles(g, 7)