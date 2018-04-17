from queue import Queue
from queue import LifoQueue


class Node:
    def __init__(self, data):
        self.data = data
        # left and right child-pointers
        self.links = [None, None]

    def __str__(self):
        return self.data


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

    def count(self, data):  # Copied
        ret = 0
        start = self.root

        while start:
            if data == start.data:
                ret += 1
                side = 0  # Check further for 'data' on left side
            else:
                side = data > start.data
            start = start.links[side]

        return ret

    # Given an existing data, find the previous and next values
    def find_prev_next(self, data):  # Copied
        if self.root is None:
            return

        current = self.root
        while current:
            if current.data == data:
                break
            side = data > current.data
            current = current.links[side]

        if not current:
            return  # data is not in tree

        if current.links[0]:
            # previous is the biggest node on left side
            start = current.links[0]
            while start.links[1]:
                start = start.links[1]
            print('Previous of ', data, 'is ', start.data)

        if current.links[1]:
            # Next is the smallest node on right side
            start = current.links[1]
            while start.links[0]:
                start= start.links[0]
            print ('Next of ', data, 'is ', start.data)

        return

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
            parent_rep = None

            while rep.links[0]:
                parent_rep = rep
                rep = rep.links[0]

            # rep is the node to replace
            current.data = rep.data
            if parent_rep:
                # rep will be on '0' side. Also, rep will not have any '0' link.
                parent_rep.links[0] = rep.links[1]
            else:
                # No parent_rep. That means, rep is on '1' side of current.
                current.links[1] = rep.links[1]
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

            # put node first, then right and left, so that it is read in reverse order
            stk.put((node, True))
            if node.links[1]:
                stk.put((node.links[1], False))
            if node.links[0]:
                stk.put((node.links[0], False))

    def _inorder(self, nod):  # Copied
        if nod:
            self._inorder(nod.links[0])
            print(nod.data, end=' ')
            self._inorder(nod.links[1])

    def inorder_r(self):  # Copied
        self._inorder(self.root)
        print('\n', '-' * 10)

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
        print('')

    def lvl_order(self):  # Copied
        q = Queue()

        if self.root:
            q.put(self.root) # No need of visited flag

        while not q.empty():
            current = q.get()
            print(current.data, end = ' ')
            if current.links[0]:
                q.put(current.links[0])
            if current.links[1]:
                q.put(current.links[1])

        print('\n', '-'*10)

    def __iter__(self):  # Copied
        self.stk = LifoQueue()  # stack should be available to __next__
        if self.root:
            self.stk.put((self.root, False))
        return self  # return object that implements __next__

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

        # Only one data in the root. So return
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
        if self.root is None or n < 1:
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
                # Travel in reverse of in-order (right, visit, left)
                if current.links[0]:  # Put left-subtree first to stack
                    stk.put((current.links[0], False))
    
                stk.put((current, True))  # Put with visited as True
                
                if current.links[1]:  # put right subtree in top of stack
                    stk.put((current.links[1], False))

        return None  # stack is empty and n is not 0

    @staticmethod
    def _height_r(start):  # Copied
        if start is None:
            return 0
        return 1 + max(BSTree._height_r(start.links[0]), \
                       BSTree._height_r(start.links[1]))

    def height_r(self):  # Copied
        return (self._height_r(self.root))

    def height(self):  # Copied
        q = Queue()
        if not self.root:
            return 0

        q.put((self.root, 1))

        while not q.empty():
            node, h = q.get()
            for i in (0, 1):
                if node.links[i]:
                    q.put((node.links[i], h + 1))

        return h

    def __del__(self):  # Copied
        if self.root is None:
            return

        q = Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            for i in (0, 1):
                if node.links[i]:
                    q.put(node.links[i])
            del node
        return

    @staticmethod
    def padding(ch, n):
        for _ in range(n):
            print(ch, end='')

    @staticmethod
    def structure(node, level):
        if not node:
            # BSTree.padding('    ', level)
            # print("~")
            pass
        else:
            BSTree.structure(node.links[1], level+1)
            BSTree.padding('    ', level)
            print(node.data)
            BSTree.structure(node.links[0], level + 1)

    def print_tree(self):
        print('-' * 20)
        BSTree.structure(self.root, 0)
        print('-' * 20)


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

    def _is_bst_rec(self, node):  # Copied
        l_val, r_val = True, True

        if node.links[0]:
            l_min, l_max, l_val = self._is_bst_rec(node.links[0])
            if not l_max <= node.data:
                return 0, 0, False
        else:
            l_max = node.data

        if node.links[1]:
            r_min, r_max, r_val = self._is_bst_rec(node.links[1])
            if not node.data < r_min:
                return 0, 0, False
        else:
            r_min = node.data

        if (l_val and r_val) is False:
            return 0, 0, False

        return l_max, r_min, True

    def is_bst_rec(self):  # Copied
        return self._is_bst_rec(self.root)[2]

    def is_bst(self):  # Copied
        # won't work for tree with duplicates because if 46 is right sub child of 46,
        # it still will be in sorted order. But rules says 46 must be left sub child.
        if not self.root:
            return True

        stk = LifoQueue()
        stk.put((self.root, False))
        last = None

        while not stk.empty():
            node, visited = stk.get()

            if visited:
                print(last, node.data)
                if last is not None and last > node.data:  # Violates binary search tree property
                    return False
                last = node.data  # Save last visited node's data
            else:
                if node.links[1]:
                    stk.put((node.links[1], False))
                stk.put((node, True))
                if node.links[0]:
                    stk.put((node.links[0], False))

        return True  # It is BST, if it dint fail before

    @staticmethod
    def _print_all_paths(node, l):  # Copied
        if node is None:
            return

        l.append(node.data)  # Add node to list
        if not any(node.links):  # Found a leaf
            print(l)
        else: # internal node
            # print all paths through left node
            BinaryTree._print_all_paths(node.links[0], l)
            # print all paths through right node
            BinaryTree._print_all_paths(node.links[1], l)

        # Done with the node. remove it
        l.pop()

    def print_all_paths(self):  # Copied
        self._print_all_paths(self.root, [])

    def print_all_paths_non_rec(self):  # Copied
        if self.root is None:
            return

        stk = LifoQueue()
        path = []
        stk.put((self.root, False))

        while not stk.empty():
            node, visited = stk.get()

            if visited:
                if not any(node.links):  # leaf
                    print(path)
                path.pop()
            else:
                stk.put((node, True))
                path.append(node.data)
                for i in (1, 0):
                    if node.links[i]:
                        stk.put((node.links[i], False))

    '''
    @staticmethod
    def _is_avl(node):
        if not node:
            return True

        if abs(BinaryTree.height(node.links[0]) - BinaryTree.height(node.links[1])) >= 2:
            return False

        return BinaryTree._is_avl(node.links[0]) and BinaryTree._is_avl(node.links[1])
    '''

    @staticmethod
    def _is_avl(node):  # copied
        if not node:
            return True, 0

        # using single recursion, calculate if node is balanced, as well as its height
        left, hl = BinaryTree._is_avl(node.links[0])
        right, hr = BinaryTree._is_avl(node.links[1])

        height = 1 + max(hl, hr)
        if abs(hl - hr) >= 2:
            return False, height

        return (left and right), height

    def is_avl(self):  # Copied
        if not self.is_bst():  # Don't forget BST check
            return False
        return BinaryTree._is_avl(self.root)[0]

    def minimum_depth(self):  # Copied
        if self.root is None:
            return -1
        q = Queue()
        q.put((self.root, 0))

        while not q.empty():
            node, lvl = q.get()

            if not any(node.links):  # Found a leaf
                return lvl
            if node.links[0]:
                q.put((node.links[0], lvl + 1))
            if node.links[1]:
                q.put((node.links[1], lvl + 1))

    # In a complete binary tree every level, except possibly the last, is completely filled,
    # and all nodes in the last level are as far left as possible.
    # It can have between 1 and 2h nodes at the last level h
    def is_complete_binary_tree(self):  # Copied
        if self.root is None:
            return True

        q = Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            if not all(node.links): # Leaves started
                if node.links[1] is not None:
                    # If only right node exists, it is not complete
                    return False
                if node.links[0] is not None: # Only left node is OK.
                    q.put(node.links[0])
                break  # break out
            q.put(node.links[0])
            q.put(node.links[1])

        # From now on, all the nodes should be leaves
        while not q.empty():
            node = q.get()
            if any(node.links):
                return False

        return True

    def is_perfect_binary_tree(self):  # Copied
        if self.root is None:
            return True

        q = Queue()
        q.put((self.root, 1))  # Root is at level 1
        prev_lvl = 0

        while not q.empty():
            node, lvl = q.get()

            if not any(node.links):  # leaves started
                if not lvl == prev_lvl + 1:  # should be a new level
                    return False
                prev_lvl = lvl
                break  # leaves started
            elif all(node.links): # internal node
                q.put((node.links[0], lvl + 1))
                q.put((node.links[1], lvl + 1))
                prev_lvl = lvl # update lvl
            else: # Node with one child
                return False

        while not q.empty():
            node, lvl = q.get()
            if any(node.links):  # Non-leaf?
                return False
            if lvl != prev_lvl:  # all leaves should be at same level
                return False

        return True

    # Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.


if __name__ == '__main__':
    bstree = BSTree()
    l = [52, 50, 98, 20, 0, 80, 34, 2, 16, 98, 56, 46, 56, 98]

    for i in l:
        bstree.insert(i)

    # bstree.inorder()
    # print()
    # print('count of 20: ', bstree.count(20))
    # print('count of 56: ', bstree.count(56))
    # print('count of 98: ', bstree.count(98))
    # print('count of 0 : ', bstree.count(0))



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

    # bstree.find_prev_next(0)
    # bstree.find_prev_next(98)
    # bstree.find_prev_next(20)

    # bstree.in_order()

    # for i in bstree:
    #     print(i, end = '*')

    '''
    a = bstree.get_first()
    print(a, end = ' ')

    while 1:
        a = bstree.get_next(a)
        if a is not None:
            print(a, end = ' ')
        else:
            break
    '''
    # print(bstree.height())
    # print(bstree.height_r())

    del bstree
    '''
    for i in {0, 2, 16, 18, 19, 20, 34, 46, 50, 52, 56, 56, 80, 98, 98, 98}:
        bstree.delete(i)
        print(i)
        bstree.in_order()
    bstree.delete(98)
    bstree.in_order()
    bstree.delete(98)
    bstree.in_order()
    bstree.delete(56)
    bstree.in_order()
    '''
#    print('')
#    bstree.inorder_r()

#    bstree.post_order()
#    print('')
#    bstree.postorder_r()

#    bstree.preorder()
#    print('')
#    bstree.preorder_r()

#    print(bstree.get_first())
#    for i in (20, 34, 80, 17, -100, 100, 3, 51, 52, 80, 97, 95, 43, 34, 18):
#        print(i, bstree.get_next(i), end = ' ** ')

#    print()
#    print(bstree.second_element(True))
#    print(bstree.second_element(False))

#    for i in range(1, 15):
#        print(bstree.nth_largest_element(i), end = ' ')

    print('')
#    print(bstree.height())
#    print(bstree.height_r())
    # bstree.delete(51)
    # bstree.delete(100)
    # for i in [18, 56, 80, 52, 2, 50, 98, 20, 16, 19, 56, 98, 34, 46]:
    #     bstree.delete_recur(i)
    #     print('deleted', i)
    #     bstree.inorder()

    print ('* ' * 10)
    binary_tree = BinaryTree()
    for i in [18, 56, 80, 52, 2, 0, 10, -5, 1, 6, 15, 40, 70, 100, 55, -10]:
        binary_tree.insert(i)

    # binary_tree.replace(2, -2)
    # print(binary_tree.is_bst_rec(), binary_tree.is_bst())
    # binary_tree.print_all_paths()
    # binary_tree.print_all_paths_non_rec()
    # print(binary_tree.minimum_depth())
    print(binary_tree.is_perfect_binary_tree())
    # binary_tree.insert(19)
    # binary_tree.insert(18)
 #   binary_tree.print_tree()
#    print(binary_tree.is_complete_binary_tree())
#    print(binary_tree.is_perfect_binary_tree())
#    print(binary_tree.is_avl())
#    binary_tree.print_all_paths()
#    print(binary_tree.minimum_depth())
#    binary_tree.print_all_paths_non_rec()
#    print(binary_tree.is_bst())
#    binary_tree.replace(34, 46)
#   binary_tree.in_order()
#   print('')
#    print(binary_tree.is_bst())