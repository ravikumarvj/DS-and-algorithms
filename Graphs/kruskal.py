### COPIED ###

class UnionFind:
    # Assume node numbers start from 1...N
    def __init__(self, N):
        self.parent = [i for i in range(N+1)]

    # Union-find's find method
    def find(self, id):  # parent is the array
        if self.parent[id] == id:  # Found the root
            return id
        # flatten the tree by assigning to parent[id]
        self.parent[id] = self.find(self.parent[id])
        return self.parent[id]

    # union-find's union method. No rank
    # make a union of sets in which id1 and id2 belongs
    def union(self, id1, id2):
        root1 = self.find(id1)
        root2 = self.find(id2)
        if root1 == root2:
            return True
        # Don't change parent[id1]. Change id1's root's parent pointer
        self.parent[root1] = root2
        return True


class EdgeGraph:
    def __init__(self):
        self.edges = []
        self.nodes = set()

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))
        self.edges.append((end, start, weight)) # Directed graph, for now
        self.nodes.add(start)
        self.nodes.add(end)


# Both prim and kruskal work with only undirected graph
def kruskal(g):
    N = len(g.nodes)
    mst = []

    # Initialize union-find data structure
    uf = UnionFind(N)

    # Sort the edges on weight
    edges = sorted(g.edges, key=lambda x:x[2])

    # Go through the sorted edges.
    for edge in edges:
        u, v, w = edge
        # if u a v are in different sets, merge them and include this edge in mst
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append(edge)
    print(mst)

if __name__ == '__main__':
    g = EdgeGraph()
    g.add_edge(1, 2, 3)
    g.add_edge(1, 5, 2)
    g.add_edge(1, 7, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 6, 4)
    g.add_edge(2, 8, 4)
    g.add_edge(3, 4, -1)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 7, 2)
    g.add_edge(6, 8, 3)


    kruskal(g)

