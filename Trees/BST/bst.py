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

    @staticmethod
    def find_smallest(start):
        while start.links[0]:
            start = start.links[0]

        return start

    @staticmethod
    def _delete_recur(data, start):
        if start is None:
            return None

        if data == start.data:
            if start.links[0] is None and start.links[1] is None:
                return None
            if start.links[0] is None:
                return start.links[1]
            if start.links[1] is None:
                return start.links[0]

            replace = Bst.find_smallest(start.links[1])
            start.data = replace.data
            start.links[1] = Bst._delete_recur(replace.data, start.links[1])
            return start

        side = data > start.data
        start.links[side] = Bst._delete_recur(data, start.links[side])
        return start

    def delete_recur (self, data):
        self.root = Bst._delete_recur(data, self.root)

    @staticmethod
    def _delete(data, start, ancestor, direction):
        current = start
        parent = ancestor
        side = direction

        while current:
            if current.data != data:
                side = data > current.data
                parent = current
                current = current.links[side]
            else:
                break
        else:
            # current is None
            return None

        if current.links[0] is None and current.links[1] is None:
            substitute = None
        elif current.links[0] is None:
            substitute = current.links[1]
        elif current.links[1] is None:
            substitute = current.links[1]

        if current.links[0] and current.links[1]:
            replace = Bst.find_smallest(current.links[1])
            current.data = replace.data
            Bst._delete(replace.data, current.links[1], current, 1)
        else:
            if parent:
                parent.links[side] = substitute
            else:
                self.root = substitute


    def delete(self, data):
        self._delete(data, self.root, None, None)


if __name__ == '__main__':
    bstree = Bst()
    l = [50, 20, 80, 34, 2, 98, 56]

    for i in l:
        bstree.insert(i)

    bstree.inorder()
    print()
    print('count of 20: ', bstree.count(20))
    print('count of 80: ', bstree.count(56))

    bstree.delete(98)

    bstree.inorder()