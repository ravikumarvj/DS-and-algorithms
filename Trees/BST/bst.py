from queue import Queue
from queue import LifoQueue


class Node:
    def __init__(self, data):
        self.data = data
        # left and right child-pointers
        self.links = [None, None]


# Bst is a binary search tree class, which allows duplicates
class BSTree:
    def __init__(self):
        self.root = None

    def search(self, data):  # Copied
        current = self.root

        while current:
            if current.data == data:
                return True
            # see which side to move: if data is <= current.data,
            # we have to move to left, or links[0/False]
            side = data > current.data
            current = current.links[side]

        return False

    def insert(self, data):  # Copied
        if self.root is None:
            # special case, root is None
            self.root = Node(data)
            return True

        current = self.root
        parent = None  # Keep parent pointer for insertion

        while current:
            # if we don't allow duplicates, below two lines are needed
            # if current.data == data:
            #      return False

            side = data > current.data

            parent = current
            current = current.links[side]

        parent.links[side] = Node(data)
        return True

    def _inorder(self, nod):  # Copied
        if nod:
            self._inorder(nod.links[0])
            print(nod.data, end = ' ')
            self._inorder(nod.links[1])

    def inorder_r(self):  # Copied
        self._inorder(self.root)
        print('\n', '-'*10)     

    def _preorder(self, nod):  # Copied
        if nod:
            print(nod.data, end=' ')
            self._preorder(nod.links[0])
            self._preorder(nod.links[1])

    def preorder_r(self):  # Copied
        self._preorder(self.root)
        print('\n', '-'*10)

    def _postorder(self, nod):  # Copied
        if nod:
            self._postorder(nod.links[0])
            self._postorder(nod.links[1])
            print(nod.data, end=' ')

    def postorder_r(self):  # Copied
        self._postorder(self.root)
        print('\n', '-'*10)

    @staticmethod # Given root and key, find the key.
    def _search(data, start):  # Copied
        current = start

        while current:
            if current.data == data:
                return current
            side = data > current.data

            current = current.links[side]

        return None

    def count(self, data): # copied
        ret = 0
        start = self.root

        while True:
            # find the occurrence of data, in a tree rooted at 'start'
            start = self._search(data, start)
            if start:
                ret += 1
            else:
                return ret
            # if data exists again, it will be on left subtree of start
            start = start.links[0]
        return ret

    @staticmethod
    def find_smallest(start):  # Copied
        while start.links[0]:
            start = start.links[0]

        return start

    @staticmethod
    def _delete_recur(data, start):  # Copied
        if start is None:
            return None

        if data == start.data:  # if data is at the start of subtree:
            if start.links[0] is None and start.links[1] is None:
                return None
            if start.links[0] is None:
                return start.links[1]
            if start.links[1] is None:
                return start.links[0]

            # Both children are present
            replace = BSTree.find_smallest(start.links[1])
            start.data = replace.data
            start.links[1] = BSTree._delete_recur(replace.data, start.links[1])
            return start # No change for start. So return start

        side = data > start.data
        start.links[side] = BSTree._delete_recur(data, start.links[side])
        return start

    def delete_recur (self, data):  # copied
        self.root = BSTree._delete_recur(data, self.root)

    def delete(self, data):  # Copied
        if self.root is None:
            return True

        current = self.root
        parent = None
        # Find the node to delete
        while current:
            if current.data != data:
                side = data > current.data
                parent = current
                current = current.links[side]
            else:
                break
        else:  # element not found
            return True

        # current is the node to delete and if parent is not None parent[side] = current
        if current.links[0] and current.links[1]:
            # Middle node deletion; Find replacement node
            rep = current.links[1]
            parent_rep = current

            if rep.links[0] is None:
                # current.links[1] is the replacement node
                current.data = rep.data
                current.links[1] = rep.links[1]
            else:
                # Loop through to find the rep
                while rep.links[0]:
                    parent_rep = rep
                    rep = rep.links[0]
                # copy data
                current.data = rep.data
                parent_rep.links[0] = rep.links[1]
        else:
            if current.links[0] is None:
                substitute = current.links[1]
            else:
                substitute = current.links[0]

            if parent:
                parent.links[side] = substitute
            else:
                self.root = substitute

        return True

    def preorder(self):  # Copied
        if self.root is None:
            return

        stk = LifoQueue()
        stk.put(self.root)

        while not stk.empty():
            node = stk.get()

            print(node.data, end = ' ')
            if node.links[1]:
                stk.put(node.links[1])
            if node.links[0]:
                stk.put(node.links[0])

    def post_order(self):  # Copied
        if self.root is None:
            return

        stk = LifoQueue()
        # Unline pre-order, we need a visited flag here, as node is visited afterwards
        stk.put((self.root, False))

        while not stk.empty():
            node, visited = stk.get()

            if visited:
                print(node.data, end = ' ')
                continue  # Continue here, as a visited node's links are already taken care

            stk.put((node, True))
            if node.links[1]:
                stk.put((node.links[1], False))
            if node.links[0]:
                stk.put((node.links[0], False))

    def in_order(self):  # Copied
        if self.root is None:
            return

        stk = LifoQueue()
        stk.put((self.root, False))

        while not stk.empty():
            node, visited = stk.get()

            if visited:
                print(node.data, end = ' ')
                continue

            if node.links[1]:
                stk.put((node.links[1], False))

            stk.put((node, True))

            if node.links[0]:
                stk.put((node.links[0], False))

    def lvl_order(self):  # Copied
        q = Queue()

        if self.root:
            q.put(self.root) # No need of visited flag

        while not q.empty():
            current = q.get()
            print(current.data, end = ' ')
            if current.links[0]:
                q.put(current.links[0])
            if (current.links[1]):
                q.put(current.links[1])

        print('\n', '-'*10)

    def __iter__(self):  # Copied
        self.stk = LifoQueue()
        if self.root:
            self.stk.put((self.root, False))
        return self

    def __next__(self):  # Copied
        while not self.stk.empty():
            node, visited = self.stk.get()
            if visited:
                return node.data
            else:
                if node.links[1]:
                    self.stk.put((node.links[1], False))
                self.stk.put((node, True))
                if node.links[0]:
                    self.stk.put((node.links[0], False))
        raise StopIteration  # Don't Forget this.

    def get_first(self):  # Copied
        if self.root is None:
            return None

        # Get the left most node's data
        current = self.root
        while current.links[0]:
            current = current.links[0]

        return current.data

    def get_next(self, data):  # Copied
        larger = None
        node = None

        if self.root is None:
            return

        current = self.root
        while current:
            if current.data > data:
                # when ever you find a node with higher data, update
                node = current
                larger = current.data

            # Loop through the data set. Note >= below
            side = data >= current.data # If data is equal, we still have to go right
            current = current.links[side]

        return larger

    def second_element(self, largest=True):  # Copied
        if self.root is None:
            return
        if self.root.links[0] is None and self.root.links[1] is None:
            return

        current = self.root
        parent = None

        # Find the largest and its parent
        while current.links[largest]:
            parent = current
            current = current.links[largest]

        # See if largest have a left sub-tree (right in case of smallest)
        # If there, is, find the largest (smallest) element there.
        # If there is no sub-tree, the parent is the second largest(smallest)

        if current.links[not largest]:
            current = current.links[not largest]
            while current.links[largest]:
                current = current.links[largest]
        else:
            current = parent

        return current.data

    '''
    @staticmethod
    def _nth_element(current):
        if not current:
            return None
        Bst._nth_element(current.links[0])
        Bst._nth_element.count -= 1
        if Bst._nth_element.count == 0:
            Bst._nth_element.ret_val = current.data
            return
        Bst._nth_element(current.links[1])



    def nth_element(self, n):
       self._nth_element.count = n
       self._nth_element(self.root)
       print(Bst._nth_element.ret_val)

       # Not- re-entrant
    '''

    def nth_largest_element(self, n):  # Copied
        if self.root is None:
            return

        stk = LifoQueue()
        stk.put((self.root, False))

        while not stk.empty():
            current, visited = stk.get()

            if visited:
                n -= 1
                if n == 0:
                    return current.data
            else:
                # Travel in reverse of inorder (right, visit, left)
                if current.links[0]:  # Put left-subtree first to stack
                    stk.put((current.links[0], False))
    
                stk.put((current, True))  # Put with visited as True
                
                if current.links[1]:  # put right subtree in top of stack
                    stk.put((current.links[1], False))

    @staticmethod
    def _height_r(start):  # Copied
        if start is None:
            return 0
        return 1 + max(BSTree._height_r(start.links[0]), \
                       BSTree._height_r(start.links[1]))

    def height_r(self):  # Copied
        return (self._height_r(self.root))

    def height(self):  # Copied
        q = LifoQueue()
        if not self.root:
            return 0

        q.put((self.root, 1))

        while not q.empty():
            node, h = q.get()
            for i in (0, 1):
                if node.links[i]:
                    q.put((node.links[i], h + 1))

        return h


class BinaryTree(BSTree):
    def replace(self, frm, to):
        q = Queue()
        if self.root is None:
            return

        q.put(self.root)

        while not q.empty():
            node = q.get()
            if node.data == frm:
                node.data = to
                return

            if node.links[0]:
                q.put(node.links[0])
            if node.links[1]:
                q.put(node.links[1])

    def is_bst(self):
        # will not work for tree with duplicates because if 46 is right sub child of 46,
        # it still will be in sorted order. But my rules says 46 should be left sub child.
        # For this, I will need to loop one extra time for checking immediate children.
        if not self.root:
            return True

        stk = LifoQueue()
        stk.put((self.root, False))
        last = None

        while not stk.empty():
            node, visited = stk.get()

            if visited:
                if last and last > node.data:  # Violates binary search tree property
                    return False
                last = node.data  # Save last visited node's data
            else:
                if node.links[1]:
                    stk.put((node.links[1], False))
                stk.put((node, True))
                if node.links[0]:
                    stk.put((node.links[0], False))

        return True  # It is BST, if it dint fail before


if __name__ == '__main__':
    bstree = BSTree()
    l = [52, 50, 20, 80, 34, 2, 16, 98, 56, 46, 56, 98]

    for i in l:
        bstree.insert(i)

    # bstree.inorder()
    # print()
    # print('count of 20: ', bstree.count(20))
    # print('count of 80: ', bstree.count(56))

    # bstree.lvl_order()

    #print(bstree.second_element(largest = False))
    #print('------------')
    #print(bstree.nth_element(5))
    #bstree.replace(52, 49)
    #bstree.inorder()
    #print(bstree.is_bst())

    # for i in bstree:
    #    print(i, end = ' ')
    # print('')

    # print(bstree.height())
    bstree.insert(19)
    bstree.insert(18)
    #    print(bstree.height())

    bstree.in_order()
    print('')
    bstree.inorder_r()

    bstree.post_order()
    print('')
    bstree.postorder_r()

    bstree.preorder()
    print('')
    bstree.preorder_r()

    print(bstree.get_first())
    for i in (20, 34, 80, 17, -100, 100, 3, 51, 52, 80, 97, 95, 43, 34, 18):
        print(i, bstree.get_next(i), end = ' ** ')

    print()
    print(bstree.second_element(True))
    print(bstree.second_element(False))

    for i in range(1, 15):
        print(bstree.nth_largest_element(i), end = ' ')

    print('')
    print(bstree.height())
    print(bstree.height_r())
    # bstree.delete(51)
    # bstree.delete(100)
    # for i in [18, 56, 80, 52, 2, 50, 98, 20, 16, 19, 56, 98, 34, 46]:
    #     bstree.delete_recur(i)
    #     print('deleted', i)
    #     bstree.inorder()

    print ('* ' * 10)
    binary_tree = BinaryTree()
    for i in l:
        binary_tree.insert(i)
    print(binary_tree.is_bst())
    binary_tree.replace(34, 46)
    binary_tree.in_order()
    print('')
    print(binary_tree.is_bst())