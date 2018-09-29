### COPIED ###
from graph_colouring import GraphNode, Graph
from queue import Queue


# Assume the graph is connected (Only one component)
def check_bipart(graph):  # Let the two colours be True and False
    start = 1  # Randomly select a node to start
    q = Queue()  # Q for BFS

    graph.vert_list[start].color = True  # Start as True
    q.put(start)

    while not q.empty():
        node_id = q.get()
        node = graph.vert_list[node_id]

        for neigh_id in node.get_neighs():
            neigh = graph.vert_list[neigh_id]
            if neigh.color:
                if neigh.color == node.color:
                    print('Not Bipart', node_id, neigh_id)
                    print(graph)
                    return False
                else:
                    pass  # Nothing to do
            else:
                # If neighbour is not coloured, give the other colour
                neigh.color = not node.color
                q.put(neigh_id)

    print('Bipart')
    print(graph)
    return True


if __name__ == '__main__':
    g = Graph()

    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    # g.add_edge(4, 6)

    check_bipart(g)