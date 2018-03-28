from digraph import DiGraph
from queue import Queue
from queue import LifoQueue


def dfs(graph, start):
    stk = LifoQueue()
    visited = set()

    stk.put(start)

    while not stk.empty():
        node_key = stk.get()
        if node_key not in visited:
            visited.add(node_key)
            print(node_key)

            node = graph.vert_list[node_key]

            for neigh in node.get_neighs():
                if neigh not in visited:
                    stk.put(neigh)


def bfs(graph, start):
    q = Queue()
    visited = set()

    q.put(start)
    visited.add(start)
    print(start)

    while not q.empty():
        node_key = q.get()
        node = graph.vert_list[node_key]

        for neigh in node.get_neighs():
            if neigh not in visited:
                q.put(neigh)
                visited.add(neigh)
                print(neigh)


if __name__ == '__main__':
    g = DiGraph()

    for i in range(10):
        g.add_vert(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    g.add_edge(6, 1, 5)
    g.add_edge(7, 5, 2)
    g.add_edge(8, 2, 4)
    g.add_edge(9, 3, 9)
    g.add_edge(1, 4, 7)
    g.add_edge(5, 8, 3)
    g.add_edge(6, 0, 1)
    g.add_edge(7, 4, 8)
    g.add_edge(8, 7, 1)
    g.add_edge(9, 6, 5)
    g.add_edge(4, 9, 2)
    g.add_edge(1, 7, 4)
    g.add_edge(7, 9, 7)

    dfs(g, 4)
