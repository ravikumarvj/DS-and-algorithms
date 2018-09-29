### COPIED ###

from digraph import DiGraph
from collections import defaultdict
from queue import Queue


class WordLadder:
    # Create a graph from the file of four letter words
    def __init__(self, filename):
        self.word_graph = DiGraph()
        # Use with for opening file
        with open(filename) as file:
            d = defaultdict(list)
            for line in file:
                word = line.strip().lower()  # Get the word
                # add 'word' in '_ord', 'w_rd', 'wo_d' and 'wor_'
                for i in range(4):  # we know its 4 letter words
                    temp = word[:i] + '_' + word[i+1:]
                    d[temp].append(word)

            # from dictionary, make graph
            for l in d.values():  # For each dictionary list,
                # add edge between all nodes
                # in 'wor_', 'work' and 'word' are neighbours
                for frm in range(len(l)):
                    for to in range(len(l)):
                        if frm != to:
                            self.word_graph.add_edge(l[frm], l[to])

    @staticmethod
    def print_path(previous, from_word, to_word):
        l = []

        node_id = to_word
        while node_id != from_word:
            l.append(node_id)
            node_id = previous[node_id]

        l.append(from_word)

        print(l[::-1])

    def find_path(self, from_word, to_word):
        if from_word == to_word:
            return

        q = Queue()  # q for BFS
        previous = {}  # Previous to store predecessor nodes

        q.put(from_word)  # add the start node to q
        previous[from_word] = None

        while not q.empty():
            node_id = q.get()
            start = self.word_graph.vert_list[node_id]

            for neigh in start.get_neighs():
                if neigh in previous:  # If neighbour is visited, continue
                    continue
                previous[neigh] = node_id
                if neigh == to_word:  # Found a path
                    self.print_path(previous, from_word, to_word)
                    return
                q.put(neigh)  # add neighbours to q
        # end of graph traversal
        print('No Path')

if __name__ == '__main__':
    puzzle = WordLadder('four_word_list.txt')
    puzzle.find_path('mail', 'made')