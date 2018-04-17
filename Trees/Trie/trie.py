from queue import LifoQueue


class Node:  # Copied
    def __init__(self, char, data = None):
        self.key = char            # current letter or digit
        self.data = data            # Data associated with node, like user's ph no.
        self.children = {}


class Trie:
    def __init__(self):  # Copied
        self.root = Node('', None)  # Root is the empty string
        self.count = 0

    def insert(self, word, data):  # Copied args: word to insert and its associated data
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c, None)  # You may insert many nodes
            node = node.children[c]

        # node is the terminal node, where 'data' should be inserted
        self.count += 1
        node.data = data

    def __len__(self):  # Copied
        return self.count

    def find_word(self, word):  # Copied
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        if node.data:
            return node.data
        return False

    def print_all1(self):  # Copied
        stk = LifoQueue()
        stk.put((self.root, False))  # start from root
        path = []

        while not stk.empty():
            node, visited = stk.get()
            if visited:
                path.pop()  # We are already done with the visited nodes.
            else:
                path.append(node.key)  # add the node's key to the path
                if node.data:
                    print(''.join(path))  # pre-order. If there is data, print it
                stk.put((node, True))  # put the node back as we will have to pop() the key
                for c in sorted(node.children, reverse=True):  # Add children in reverse order
                    stk.put((node.children[c], False))

    @staticmethod
    def _print_all(node, string):  # Copied
        string.append(node.key)
        if node.data:  # First take care of this node (pre-order)
            print(''.join(string))
        for c in sorted(node.children):  # Use sorted to get ascending order
            Trie._print_all(node.children[c], string)
        string.pop()  # done with the key of this node

    def print_all2(self):  # Copied
        string = []
        self._print_all(self.root, string)

    def print_all_prefix(self, prefix):  # copied
        node = self.root
        string = []
        for c in prefix:
            if c not in node.children:
                return
            string.append(node.key)  # Dont forget
            node = node.children[c]

        self._print_all(node, string)

    def delete_word(self, word):  # Copied
        if word is None or len(word) == 0:  # HAve this kind of check for all function
            return
        node = self.root
        stk = LifoQueue()

        for c in word:
            if c not in node.children:  # Don't write as 'if not node.children[c]:'
                return
            stk.put(node)  # self.root also added. Take care not to delete that
            node = node.children[c]

        if node.data is None:
            return

        # This is the node to delete
        node.data = None
        self.count -= 1

        while not stk.empty():
            if node.data is not None or len(node.children):
                return

            parent = stk.get()
            del parent.children[node.key]  # Don't write 'parent.children[node.key] = None'
            del node
            node = parent  # when parent is self.root, stk.empty will be True

    @staticmethod
    def _find_single_char(node, word, diff):  # Copied
        if word is None or len(word) == 0: # don't forget. Especially in this problem.
            return

        # print(word, diff)
        chars = 'abcdefghijklmnopqrstuvwxyz'  # Make this as class variable
        # if diff == 0, no character change done so far
        if diff == 0:
            for i in chars:
                if i not in node.children:
                    continue
                if i != word[0]:
                    # made single character change
                    Trie._find_single_char(node.children[i], word[1:], 1)
                else:
                    # No character change. Do it in next step
                    Trie._find_single_char(node.children[i], word[1:], 0)
        else:
            # Done a character change. Traverse down and see if there is a word.
            # Here also, we could do only single step-by-step, if needed. But is un-necessary
            for c in word:
                if c not in node.children:
                    return
                node = node.children[c]

            if node.data:
                print(node.data)

    # Given a word, find all the words with only a single character different
    def find_word_single_char(self, word):  # Copied
        self._find_single_char(self.root, word, 0)


if __name__ == '__main__':
    trie = Trie()

    # word_list = ['ravi', 'rejitha', 're', 'raju', 'ram', 'rem', 'rice', 'saw', 'sit']
    # for i in word_list:
    #    trie.insert(i, i)
    with open('wordlist.txt') as fil:
        for word in fil:
            word = word.strip()
            trie.insert(word, word)

    trie.find_word_single_char('differance')
    # print(trie.find_word('ravi'))
    # print(trie.find_word('rajitha'))
    # print('-' * 10)
    # trie.print_all1()
    # print('*' * 10)
    # trie.print_all2()
    # print('-' * 10)
    # trie.print_all_prefix('ri')
    # trie.delete_word('rem')
    # trie.delete_word('re')
    # trie.delete_word('rejitha')
    # for i in ['ravi', 'rejitha', 're', 'raju', 'ram', 'rem', 'rice', 'saw', 'sit']:
    #     trie.delete_word(i)
    # trie.print_all1()
    # print(trie.root.children)
