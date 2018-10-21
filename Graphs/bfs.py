### COPIED ###  VERIFIED

from digraph import DiGraph
from queue import Queue
from queue import LifoQueue
from graph import NGraph
from time import time

vis = set()

def dfs_rec_alt_r(graph, start, visited):
    print(start, end=' ')
    for neigh in sorted(graph.vert_list[start].get_neighs()):
        if neigh not in visited:
            visited.add(neigh)
            dfs_rec_alt_r(graph, neigh, visited)

def dfs_rec_alt(graph, start):
    visited = set()
    visited.add(start)
    dfs_rec_alt_r(graph, start, visited)

# Recursive implementation of DFS
def dfs_rec(graph, start):
    vis.add(start)
    print(start, end=' ')

    for neigh in sorted(graph.vert_list[start].get_neighs()):
        if neigh not in vis:
            dfs_rec(graph, neigh)
    # print(start, end=' ')  # Post-order printing

# Optimized for stack. But not true DFS. We don't reach the end, even if
# there are unvisited nodes, before back-tracking. This is because we
# are adding the visited flag when adding to stack. Ex: 1->2, 1->3, 1->5, 2->5
# will be travelled in order 1, 2, 3, 5 rather than 1, 2, 5, 3
def dfs_better(graph, start):
    stk = LifoQueue()
    visited = set()

    stk.put(start)
    visited.add(start)

    while not stk.empty():
        node_id = stk.get()
        node = graph.vert_list[node_id]
        print(node_id, end = ' ')

        for neigh in sorted(node.get_neighs(), reverse=True):
            # If not visited, make it visited and add to stack
            if neigh not in visited:
                stk.put(neigh)
                visited.add(neigh)

    print('')


# same output as recursive DFS. But we will have duplicate entries in the queue and hence slow.
# For example, if there is a graph with 1->2, 1->5 and 2->5, first we will add 5 as neighbour of 1
# we will again add 5 as neighbour of 2
def dfs(graph, start):
    stk = LifoQueue()
    visited = set()

    stk.put(start)

    while not stk.empty():
        node_key = stk.get()
        # Take from stack. If not visited, visit
        if node_key not in visited:
            visited.add(node_key)
            print(node_key, end = ' ')

            node = graph.vert_list[node_key]

            for neigh in sorted(node.get_neighs(), reverse=True):
                if neigh not in visited:
                    stk.put(neigh)
    print('')


def bfs(graph, start):
    q = Queue()
    visited = set()

    q.put(start)
    # Unlike DFS, make visited when adding to q.
    visited.add(start)

    while not q.empty():
        node_key = q.get()
        node = graph.vert_list[node_key]
        # Process on taking out of queue. Same as processing on adding to q
        print(node_key, end=' ')

        for neigh in node.get_neighs():
            if neigh not in visited:
                q.put(neigh)
                visited.add(neigh)
    print()

if __name__ == '__main__':
    g = NGraph()

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

    # print(g)
    # t = time()
    # dfs(g, 4)
    # print(time() - t)

    # t = time()
    # dfs_better(g, 4)
    # print(time() - t)

    dfs_rec(g, 4)
    print('')
    dfs_rec_alt(g, 4)
    # print('')

    # bfs(g, 4)