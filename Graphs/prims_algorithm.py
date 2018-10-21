### COPIED ###  VERIFIED
from graph import NGraph
from priority_queue import PriorityQueue


def prims_mst_alt(g):
    visited = set()  # visited set, already in MST
    pq = PriorityQueue()  # For edges
    mst = []  # result as a list of edges
    N = g.num_vert

    start = 5  # Arbitrarily choose a start node.

    while len(mst) < N-1:
        node = g.vert_list[start]
        visited.add(start)
        # Check all the neighbours and add them to PQ if needed.
        for neigh in node.get_neighs():
            if neigh not in visited:
                key = node.get_weight(neigh)
                edge = (start, neigh, key)
                pq.decrease_priority(edge, key)

        while pq.length > 0:
            u, v, w = pq.extract_min()
            if v not in visited:
                break
        else:
            print('disconnected')
            return
        mst.append((u, v, w))
        start = v

    print(mst)


def prims_mst(g):
    visited = set()  # visited set, already in MST
    distance = {}  # edge-distance to add the node to MST
    previous = {}
    pq = PriorityQueue()

    start = 5  # Arbitrarily choose a start node.
    for node in g.get_vertices():
        distance[node] = float('inf')
        previous[node] = None

    distance[start] = 0
    pq.add_with_priority(start, 0)

    while pq.length > 0:
        node_id = pq.extract_min()

        visited.add(node_id)  # Add node to MST
        node = g.vert_list[node_id]

        # Check all the neighbours and add them to PQ if needed.
        for neigh in node.get_neighs():
            if neigh not in visited:
                # A node may be neigh of many nodes which are in MST
                if node.get_weight(neigh) < distance[neigh]:
                    # Unlike dijkstra, just replace the distance with new edge.
                    distance[neigh] = node.get_weight(neigh)
                    previous[neigh] = node_id
                    pq.decrease_priority(neigh, distance[neigh])

    print(previous)
    print(distance)


if __name__  == '__main__':
    g = NGraph()
    g.add_edge(1, 2, -1)
    g.add_edge(1, 3, 4)
    # g.add_edge(1, 6, 3)
    g.add_edge(2, 3, 2)
    # g.add_edge(2, 5, 6)
    g.add_edge(2, 8, 3)
    g.add_edge(3, 4, 1)
    # g.add_edge(3, 5, 3)
    # g.add_edge(4, 6, 2)
    g.add_edge(5, 6, 12)
    # g.add_edge(5, 7, 8)
    # g.add_edge(6, 7, -1)
    g.add_edge(7, 8, 1)

    prims_mst(g)
    prims_mst_alt(g)