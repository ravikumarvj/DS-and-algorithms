### COPIED ####  VERIFIED
"""
Given an undirected graph represented as an adjacency matrix and an integer k,
determine whether each node in the graph can be colored such that no
two adjacent nodes share the same color using at most k colors.
"""

def get_neigh(start, graph):
    ret = []
    for i in range(len(graph[start])):
        if graph[start][i] == 1:
            ret.append(i)
    return ret

def _can_color(start, graph, colour_given, visited, colour_set):
    visited.add(start)  # Make start as visited
    neighbours = get_neigh(start, graph)   # Get all neighbours of start

    # colour_used is the set of colours used by the neighbouts
    colour_used = {colour_given[i] for i in neighbours if colour_given[i] != 0}  # set because, there coult be duplicates

    # If there is no colour that can be given for start, return False, and make start as un-visited
    if len(colour_used) == len(colour_set):
        visited.remove(start)  # This path wont work. Remove start from visited. No colour yet given
        return False

    # Give a un-used colour to start, one by one
    for c in colour_set:

        # Give one of the free colour to start and visit its un-visited neighbours
        if c not in colour_used:
            colour_given[start] = c

            # If all nodes are given colour, retutrn True
            if len(visited) == len(graph):
                print(c, start, visited)
                print(colour_given)
                return True

            for i in neighbours:
                if i not in visited:
                    if _can_color(i, graph, colour_given, visited, colour_set) is True:
                        return True

    # visited.remove(start)
    # colour_given[start] = 0
    return False

def can_color(graph, k):
    n = len(graph)
    visited = set()  # Visited node
    colour_given = [0] * n   # colours given for each node
    colour_set = {i for i in range(1, k+1)}   # Available colours

    return _can_color(0, graph, colour_given, visited, colour_set)


if __name__ == '__main__':
    graph = [[0, 1, 1, 1, 1, 1],
             [1, 0, 1, 1, 1, 0],
             [1, 1, 0, 1, 1, 1],
             [1, 1, 1, 0, 1, 0],
             [1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0]]

    k = 4
    print(can_color(graph, k))
