from graph_p import Graph


class DiGraph(Graph):
    def add_edge(self, from_key, to_key, weight=1):
        # add the vertices first
        self.add_vert(from_key)
        self.add_vert(to_key)

        # call vertex method to set the edge
        self.vert_list[from_key].add_neigh(to_key, weight)


if __name__ == '__main__':
    g = DiGraph()

    for i in range(6):
        g.add_vert(i)

    print(g.get_vertices())

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        print(v)