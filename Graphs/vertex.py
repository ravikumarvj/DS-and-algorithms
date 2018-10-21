### COPIED ###  VERIFIED
class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighs = {} # No multiple edges to same neighbour

    # Add edge from this vertex with given weight to neigh_key
    def add_neigh(self, neigh_key, weight = 1):
        self.neighs[neigh_key] = weight

    # return a list of neighbours
    def get_neighs(self):
        return self.neighs.keys()

    # get the weight to a neighbour
    def get_weight(self, neigh_key):
        if neigh_key in self.neighs:
            return self.neighs[neigh_key]

    def __str__(self):
        return str(self.key) + ' is connected to: ' + \
               ', '.join((str(i) + '[' + str(j) + ']' for i, j in self.neighs.items()))