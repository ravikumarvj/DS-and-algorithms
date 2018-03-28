from graph_p import Graph


class Digraph(Graph):
    def add_edge(self, from_key, to_key, weight=1):
        # add the vertices first
        self.add_vert(from_key)
        self.add_vert(to_key)

        # call vertex method to set the edge
        self.vert_list[from_key].add_neigh(to_key, weight)
