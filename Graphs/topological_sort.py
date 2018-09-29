### COPIED ###
from digraph import DiGraph


class CycleException(Exception):
    pass


def depth_traversal(g, node, visited, topology):
    visited[node] = 1  # start processing

    for neigh in g.vert_list[node].get_neighs():
        if visited[neigh] == 1:  # found a node in processing
            raise CycleException("Graph contains cycle")
        if visited[neigh] == 2:  # ignore visited node
            continue
        # Recursively do DFS
        depth_traversal(g, neigh, visited, topology)

    visited[node] = 2  # make the node visited
    topology.append(node) # Add to topology list


def topological_sort(g):
    visited = {}
    topology = []  # Stack for storing the ordering

    # we need 3 flags (0, 1, 2) to check if there is a cycle.
    # 0=not visited, 1=in the process, 2=visited
    for node in g.get_vertices():
        visited[node] = 0

    # Go through each non-visited node and start a DFS from that node
    for node in g.get_vertices():
        if visited[node] != 2:
            depth_traversal(g, node, visited, topology)

    # Reverse the topology and print
    print(topology[::-1])
    return topology[::-1]

if __name__ == '__main__':
    g = DiGraph()
    g.add_edge(6, 3)
    g.add_edge(3, 7)
    g.add_edge(3, 2)
    g.add_edge(1, 2)
    g.add_edge(10, 1)
    # g.add_edge(2, 8)
    # g.add_edge(5, 9)
    # g.add_edge(5, 4)
    # g.add_edge(4, 8)
    # g.add_edge(8, 6)
    try:
        topological_sort(g)
    except CycleException:
        print('Graph contains Cycle')
