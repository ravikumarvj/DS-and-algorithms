from digraph import DiGraph
from collections import defaultdict
from queue import Queue


def make_graph(file_name):
    init_dict = defaultdict(list)
    graph = DiGraph()

    f = open(file_name)

    for line in f:
        word = line.strip()
        for k in range(len(word)):
            temp = word[:k] + '_' + word[k+1:]
            init_dict[temp].append(word)

    for i in init_dict:
        for frm in init_dict[i]:
            for to in init_dict[i]:
                if frm != to:
                    graph.add_edge(frm, to)

    return graph

def find_path(graph, from_word, to_word):
    q = Queue()
    visited = {}

    q.put((from_word, graph.vert_list[from_word]))
    visited[from_word] = (None, graph.vert_list[from_word])
    while not q.empty():
        key, vert = q.get()

        for neigh in vert.neighs:
            if neigh not in visited:
                q.put((neigh, graph.vert_list[neigh]))
                visited[neigh] = (key, graph.vert_list[neigh])

                if neigh == to_word:
                    break
        if neigh == to_word:
            break

    if to_word in visited:
        print('found path')
        l = []
        word = to_word
        while word != from_word:
            l.append(word)
            word = visited[word][0]
        l.append(from_word)
        print(l[::-1])


if __name__ == '__main__':
    graph = make_graph('four_word_list.txt')

    find_path(graph, "film", "fool")