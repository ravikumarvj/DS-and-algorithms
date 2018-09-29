### COPIED ###

from digraph import DiGraph
"""
Using edge-list implementation
"""


class EdgeGraph:
    def __init__(self):
        self.edges = []  # Edge list
        self.nodes = set() # nodes

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))
        # self.edges.append((end, start, weight)) # Directed graph, for now
        self.nodes.add(start)
        self.nodes.add(end)


def bellman_ford(g, start):
    distance = {}  # Distance from start
    previous = {}  # Previous node to reach the node
    N = len(g.nodes)  # Total number of nodes

    for node in g.nodes:
        distance[node] = float('inf')
        previous[node] = None
    distance[start] = 0  # distance from start to start is 0

    # NO PQ or anything. Just a loop of N-1
    for i in range(N - 1):  # N-1 repetitions
        for edge in g.edges:  # Go through edges one by one
            u, v, w = edge
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                previous[v] = u

    # Checking for cycles
    for edge in g.edges:
        u, v, w = edge
        if distance[u] + w < distance[v]:
            # still possible to reduce distance
            print('Contains negative cycle', u, v, w, distance[u], distance[w])
            return

    print(distance)
    print(previous)


"""
Using normal graph
"""
def bellman_ford_2(g, start):
    distance = {}
    previous = {}
    N = g.num_vert

    for node in g.get_vertices():
        distance[node] = float('inf')
        previous[node] = None
    distance[start] = 0

    for i in range(N - 1):
        # All edges' traversal
        for node in g:  # Go through all the nodes and get its neighbours
            for neigh in node.get_neighs():
                u = node.key
                v = neigh
                w = node.get_weight(v)
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    previous[v] = u

    for node in g:
        for neigh in node.get_neighs():
            u = node.key
            v = neigh
            w = node.get_weight(v)
            if distance[u] + w < distance[v]:
                print('Contains negative cycle', u, v, w, distance[u], distance[w])
                return
    print(distance)
    print(previous)


"""
Special case: Bellman ford on DAG
"""
from topological_sort import topological_sort
def bellman_ford_3(g, start):
    # Do a topological sort. Get back the list of node in topological ordering
    topo = topological_sort(g)

    # Initialize a distance dictionary. Infinity distance to all nodes, except start
    distance = {}
    for node in g.get_vertices():
        distance[node] = float('inf')
    distance[start] = 0

    # Find out start node. Distance to all nodes before it will be always infinity
    for i in range(len(topo)):
        if topo[i] == start:
            break
    # Now, topo[i] will contain the start node. Any edge starting from it,
    # will be only towards nodes coming after it.

    # One pass of bellman ford. Go through all the edges of nodes from start node
    for i in range(i, len(topo)): # Go through all nodes including start.
        node_id = topo[i]
        node = g.vert_list[node_id]
        for neigh in node.get_neighs():
            n_wait = node.get_weight(neigh)
            if distance[neigh] > distance[node_id] + n_wait:
                distance[neigh] = distance[node_id] + n_wait

    print(distance)

if __name__ == '__main__':
    g = EdgeGraph()

    g.add_edge(1, 3, 4)
    g.add_edge(1, 6, 3)
    g.add_edge(2, 1, -1)
    g.add_edge(2, 5, 6)
    g.add_edge(3, 2, 2)
    g.add_edge(3, 4, 1)
    g.add_edge(4, 6, 2)
    g.add_edge(5, 3, 3)
    g.add_edge(5, 6, -2)
    g.add_edge(6, 7, -1)
    g.add_edge(7, 5, 8)

    bellman_ford(g, 1)
    g = DiGraph()

    g.add_edge(1, 3, 4)
    g.add_edge(1, 6, 3)
    g.add_edge(2, 1, -1)
    g.add_edge(2, 5, 6)
    g.add_edge(3, 2, 2)
    g.add_edge(3, 4, 1)
    g.add_edge(4, 6, 2)
    g.add_edge(5, 3, 3)
    g.add_edge(5, 6, -2)
    g.add_edge(6, 7, -1)
    g.add_edge(7, 5, 8)

    bellman_ford_2(g, 1)
    print('****')
    g = DiGraph()
    g.add_edge(0, 1, -4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 6)
    g.add_edge(1, 4, 2)
    g.add_edge(2, 1, -8)
    g.add_edge(4, 3, -5)
    g.add_edge(5, 3, 4)
    g.add_edge(6, 3, -2)

    bellman_ford_3(g, 0)