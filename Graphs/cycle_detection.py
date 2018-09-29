### COPIED ###
from digraph import DiGraph
from graph import NGraph


def cycle_dfs(g, start, visited):
    visited[start] = 1  # processing
    for neigh in g.vert_list[start].get_neighs():
        if visited[neigh] == 1:
            print('contain Cycle')
            return True
        if visited[neigh] != 2:
            if cycle_dfs(g, neigh, visited):
                return True

    visited[start] = 2  # Done with start
    return False


def cycle_directed(g):
    # visited size depends on node numbering
    visited = [0] * (g.num_vert + 1)

    for node in g:  # loop through all the nodes
        if visited[node.key] != 2:
            if cycle_dfs(g, node.key, visited):
                return True
    print('No cycle')


# For undirected, pass the parent node also, so as to ignore the same edge
# For undirected graph, there is no need of processing flag as we
# can reach any node from any other node within connected component
# As soon as it is taken out of stack, node can be moved to visit.
def cycle_dfs_u(g, start, visited, predecessor):
    visited[start] = True  # processing
    count = 0 # Count kept for back edge

    for neigh in g.vert_list[start].get_neighs():
        # Consider edge going to same start, if it appears more than once
        if neigh == predecessor:
            count += 1  # untested as my graph-vertex uses dict() to store neighs

        # if visited[neigh] == True and neigh != predecessor: # No back-edge allowed
        if visited[neigh] == True and (neigh != predecessor or count > 1):
            print('contain Cycle')
            return True

        # Do only when it is not processing and not visited. Check directed diff.
        if visited[neigh] is False:
            # pass start as the predecessor of neigh
            if cycle_dfs_u(g, neigh, visited, start):
                return True

    return False


def cycle_undirected(g):
    visited = [False] * (g.num_vert + 1)

    for node in g:  # loop through all the nodes
        if visited[node.key] != True:
            if cycle_dfs_u(g, node.key, visited, -1):
                return True
    print('No cycle')



if __name__ == '__main__':
    g = DiGraph()
    g.add_edge(3, 2)
    g.add_edge(4, 5)
    g.add_edge(5, 2)
    g.add_edge(5, 3)
    g.add_edge(3, 1)
    g.add_edge(6, 5)
    # cycle_directed(g)

    g = NGraph()
    g.add_edge(1, 5)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(3, 6)
    g.add_edge(3, 2)
    g.add_edge(2, 6)
    cycle_undirected(g)