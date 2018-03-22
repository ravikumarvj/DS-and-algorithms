class Node:
    def __init__(self, data):
        self.data = data
        self.links = [None, None]


# Bst is a binary search tree class, which allows duplicates
class Bst:
    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root

        while current:
            if current.data == data:
                return True
            side = data > current.data

            current = current.links[side]

        return False

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return True

        current = self.root
        parent = None

        while current:
#           if current.data == data:
#               return False

            side = data > current.data

            parent = current
            current = current.links[side]

        parent.links[side] = Node(data)
        return True


    def _inorder(self, nod):
        if nod:
            self._inorder(nod.links[0])
            print(nod.data, end = ' ')
            self._inorder(nod.links[1])

    def inorder(self):  
        self._inorder(self.root)    
    
    def _search(self, data, start):
        current = start

        while current:
            if current.data == data:
                return current
            side = data > current.data

            current = current.links[side]

        return None

    def count(self, data):
        ret = 0
        start = self.root

        while True: 
            start = self._search(data, start)
            if start:
                ret += 1
            else:
                return ret
            start = start.links[0]
        return ret


if __name__ == '__main__':
    bstree = Bst()
    l = [50, 20, 80, 34, 2, 98, 56, 56, 74, 56, 120, 11, 89, 20, 56, 20]

    for i in l:
        bstree.insert(i)

    bstree.inorder()
    print()
    print('count of 20: ', bstree.count(20))
    print('count of 80: ', bstree.count(56))
