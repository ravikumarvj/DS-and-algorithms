from vertex import Vertex
from abc import ABCMeta, abstractmethod


class Graph:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.vert_list = {}  # list of vertices
        self.num_vert = 0

    def add_vert(self, vert_key):
        if vert_key not in self.vert_list:  # if not already there, create vertex
            self.vert_list[vert_key] = Vertex(vert_key)
            self.num_vert += 1
        return True

    def __contains__(self, vert_key):
        return vert_key in self.vert_list

    @abstractmethod
    def add_edge(self, from_key, to_key, weight=1):
        pass

    # Get list of vertices
    def get_vertices(self):
        return self.vert_list.keys()

    # iterate through all vertex objects
    def __iter__(self):
        # return iter of list (ver_list.values), which already have __next__
        return iter(self.vert_list.values())

    def __str__(self):
        for i in sorted(self.vert_list.keys()):
            print(self.vert_list[i])
        return '' # __str__ must return a string
