### COPIED ###  VERIFIED

from vertex import Vertex

class GraphNode (Vertex):
    def __init__(self, key):
        self.key = key
        self.neighs = {}
        self.color = None

    def __str__(self):
        return str(self.key) + ' with ' + str(self.color) + ' is connected to: ' + \
               ', '.join((str(i) + '[' + str(j) + ']' for i, j in self.neighs.items()))

class Graph:
    def __init__(self):
        self.vert_list = {}  # list of vertices
        self.num_vert = 0

    def __contains__(self, vert_key):
        return vert_key in self.vert_list

    def add_vert(self, vert_key):
        if vert_key not in self.vert_list:  # if not already there, create vertex
            self.vert_list[vert_key] = GraphNode(vert_key)
            self.num_vert += 1
        return True

    def add_edge(self, from_key, to_key, weight=1):
        # add the vertices first
        self.add_vert(from_key)
        self.add_vert(to_key)

        # call vertex method to set the edge, both ways
        self.vert_list[from_key].add_neigh(to_key, weight)
        self.vert_list[to_key].add_neigh(from_key, weight)

    # Get list of vertices
    def get_vertices(self):
        return self.vert_list.keys()

    # iterate through all vertex objects
    def __iter__(self):
        # return iter of list (ver_list.values), which already have __next__
        return iter(self.vert_list.values())

    def __str__(self):
        ret = ''
        for i in sorted(self.vert_list.keys()):
            # print(self.vert_list[i])  # __str__ must return a string. So instead of printing, we return str
            ret = ret + str(self.vert_list[i]) + '\n'
        return ret


def colour_graph(g, colours):
    for node in g:  # O(N)
        if node.color is not None:
            continue

        # Combined with the above for loop, getting all vertices is O(M), where M is number of edges
        # For all nodes, get neighbours. Total no. of neighs is 2 * M.
        done_c = {g.vert_list[node].color for node in node.get_neighs() if g.vert_list[node].color}

        # unused = colours - done_c  # Set difference s-t is O(len(s))
        for color in colours:        # O(D). But combined with for-loop, this is O(M)
            if color not in done_c:  # O(1)
                node.color = color
                break


if __name__ == '__main__':
    g = Graph()
    colours = {'blue', 'green', 'red', 'yellow'}  # max degree 3

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 4)
    g.add_edge(3, 8)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 9)

    colour_graph(g, colours)

    print(g)