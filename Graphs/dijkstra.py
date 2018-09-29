### COPIED ###

from graph import NGraph
from digraph import DiGraph
from priority_queue import PriorityQueue


def dijkstra(g, start):
    # Distance is the priority in PQ
    pq = PriorityQueue()
    visited = set()  # Redundant as weighs are always positive
    distance = {}  # Store distance to nodes from start
    previous = {}  # Store the previous node to reach a node

    # Set all the weight to infinity
    for node_id in g.get_vertices():
        distance[node_id] = float('inf') # infinity
    distance[start] = 0  # start to start have zero distance
    previous[start] = None  # No previous for start
    # Add start to priority queue
    pq.add_with_priority(start, 0)

    while pq.length > 0:  # PQ will have unvisited nodes
        node_id = pq.extract_min()
        node = g.vert_list[node_id]

        for neigh in node.get_neighs():
            if neigh not in visited:
                n_dist = node.get_weight(neigh)
                # if distance to neigh is less through, node_id, update.
                if distance[node_id] + n_dist < distance[neigh]:
                    distance[neigh] = distance[node_id] + n_dist
                    previous[neigh] = node_id
                    # Update/add neigh in PQ, with new distance
                    pq.decrease_priority(neigh, distance[neigh])
        # Done processing the node. Mark it as visited
        visited.add(node_id)

    print(distance)
    print(previous)

def dijkstra(g, start):
    # Distance is the priority in PQ
    pq = PriorityQueue()
    visited = set()  # Redundant as weighs are always positive
    distance = {}  # Store distance to nodes from start
    previous = {}  # Store the previous node to reach a node

    # prepare the start node
    distance[start] = 0  # start to start have zero distance
    previous[start] = None  # No previous for start
    # Add start to priority queue
    pq.add_with_priority(start, 0)

    while pq.length > 0:  # PQ will have unvisited nodes
        node_id = pq.extract_min()
        node = g.vert_list[node_id]

        for neigh in node.get_neighs():
            if neigh not in visited:
                n_dist = node.get_weight(neigh)
                # if distance to neigh is less through, node_id, update.
                if neigh not in distance or distance[node_id] + n_dist < distance[neigh]:
                    distance[neigh] = distance[node_id] + n_dist
                    previous[neigh] = node_id
                    # Update/add neigh in PQ, with new distance
                    # Here, decrease_priority will add as well as update.
                    # If such is not available, we will have to prepare PQ with
                    # all nodes with float('inf') distance, except start
                    pq.decrease_priority(neigh, distance[neigh])
        # Done processing the node. Mark it as visited
        visited.add(node_id)

    print(distance)
    print(previous)

if __name__ == '__main__':
    g = NGraph()
    g.add_edge(1, 7, 4)
    g.add_edge(1, 8, 3)
    g.add_edge(2, 4, 8)
    g.add_edge(2, 5, 2)
    g.add_edge(3, 8, 8)
    g.add_edge(3, 9, 9)
    g.add_edge(3, 10, 4)
    g.add_edge(4, 11, 5)
    g.add_edge(5, 6, 1)
    g.add_edge(5, 9, 3)
    g.add_edge(5, 10, 9)
    g.add_edge(6, 7, 8)
    g.add_edge(9, 10, 5)
    g.add_edge(9, 12, 10)
    g.add_edge(11, 12, 2)

    dijkstra(g, 1)

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

    dijkstra(g, 1)