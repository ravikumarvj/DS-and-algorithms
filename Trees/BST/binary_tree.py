from bst import BSTree, Node
from queue import Queue


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

    @staticmethod
    def find(node, data):  # Copied
        if node is None:
            return False

        if node.data == data:
            return True

        return BinaryTree.find(node.links[0], data) or BinaryTree.find(node.links[1], data)

    # No need of find method and tuple returning, if we assume a and b to be present in tree.
    @staticmethod
    def _find_common_ancestor(node, a, b):  # Assume a != b  # Copied
        if node is None:
            return None, False, False
        if node.data == a:
            ret = BinaryTree.find(node, b)
            return a, True, ret
        if node.data == b:
            ret = BinaryTree.find(node, a)
            return b, ret, True

        left, found_l_a, found_l_b = BinaryTree._find_common_ancestor(node.links[0], a, b)
        right, found_r_a, found_r_b = BinaryTree._find_common_ancestor(node.links[1], a, b)

        if left is not None and right is not None:
            return node.data, found_l_a or found_r_a, found_l_b or found_r_b

        return (left, found_l_a, found_l_b) if left is not None else (right, found_r_a, found_r_b)

    def find_common_ancestor(self, a, b):  # Copied
        parent, a_f, b_f = BinaryTree._find_common_ancestor(self.root, a, b)
        if a_f and b_f:
            print(parent)
            return parent
        if a_f:
            print(b, 'is not present')
        else:
            print(a, 'is not present')
        return None

    @staticmethod
    def _find_common_ancestor_present(node, a, b):  # Copied
        if node is None:
            return None
        if node.data == a:
            return a
        if node.data == b:
            return b

        left = BinaryTree._find_common_ancestor_present(node.links[0], a, b)
        right = BinaryTree._find_common_ancestor_present(node.links[1], a, b)

        if left is not None and right is not None:
            return node.data

        return left if left is not None else right

    def find_common_ancestor_present(self, a, b):  # Copied
        return BinaryTree._find_common_ancestor_present(self.root, a, b)

    # assume a != b. Don't assume and b to exist
    def find_common_ancestor_iterative(self, a, b):  # Copied
        if self.root is None:
            return
        stk = LifoQueue()
        stk.put((self.root, False))
        path = []
        path_a, path_b = None, None

        while not stk.empty():
            node, visited = stk.get()
            if visited:
                if node.data == a:  # Found path to a
                    path_a = path.copy()
                elif node.data == b:  # Found path to b
                    path_b = path.copy()
                path.pop()
                if path_a and path_b:  # Found both path. Break out
                    break
            else:
                stk.put((node, True))
                path.append(node.data)

                if node.links[1]:
                    stk.put((node.links[1], False))
                if node.links[0]:
                    stk.put((node.links[0], False))

        # one or both of a and b dont exist
        if path_a is None or path_b is None:
            print(None)
            return

        for i, j in zip(path_a, path_b):
            if i == j:
                ans = i
            else:
                break

        print(ans)

    def count_universal_subtrees(self):
        return self._count_univ_st(self.root)

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
            BinaryTree.structure(node.links[1], level+1)
            BinaryTree.padding('    ', level)
            print(node.data)
            BinaryTree.structure(node.links[0], level + 1)

    def print_tree(self):
        print('-' * 20)
        BinaryTree.structure(self.root, 0)
        print('-' * 20)

    @staticmethod
    def _count_univ_st(root):
        if root is None:
            return 0, True  # second argument passed is to see if the root is part of the same unival subtree or not
        if root.links[0] is None and root.links[1] is None:
            return 1, True  # leaf is a unival subtree. True because this node is part of subtree

        # Count unival subtrees on right and left
        left_count, left_same = BinaryTree._count_univ_st(root.links[0])
        rite_count, rite_same = BinaryTree._count_univ_st(root.links[1])

        add = left_count + rite_count

        if left_same and rite_same:
            if root.links[0] and root.links[0].data != root.data:
                return add, False
            if root.links[1] and root.links[1].data != root.data:
                return add, False
            return 1 + add, True  # Both left side and rite side are same as root.data and both returned True

        return add, False

    @staticmethod
    def _find_bstree(node):   ## COPIED
        """
        :return: 1. Size of largest bst,
                 2. if this (root)node is part of the BST
                 3. Biggest value of this BST (dont care if 2 is False)
                 4. Smallest value of the BST (dont care if 2 is False)
        """
        if node is None:
            # biggest = -infinity; smallest = infinity
            return 0, True, -float('inf'), float('inf')


        # If left is not there, biggest_l = -inf, smallest_l = inf
        size_l, truth_l, biggest_l, smallest_l = BinaryTree._find_bstree(node.links[0])
        # if right is not there, biggest_r= -inf, smallest_r = inf
        size_r, truth_r, biggest_r, smallest_r = BinaryTree._find_bstree(node.links[1])

        if truth_l and truth_r:  # both side are bst
            # node should be between largest of left and smallest of right
            if biggest_l < node.data < smallest_r:  # Allows equal elements.
                # in this BST, biggest will be biggest_r and smallest will be smallest_l
                # if biggest_r is -inf, choose node.data as biggest
                biggest = max(biggest_r, node.data)
                # if smallest_l is inf, choose node.data as smallest
                smallest = min(smallest_l, node.data)
                return size_l + 1 + size_r, True, biggest, smallest

        return (size_l if size_l > size_r else size_r), False, 0, 0

    def find_bstree(self):  ## COPIED
        if self.root is None:
            return 0
        return BinaryTree._find_bstree(self.root)[0]



if __name__ == '__main__':
    binary_tree = BinaryTree()
    for i in [18, 56, 80, 52, 2, 0, 10, -5, 1, 6, 15, 40, 70, 100, 55, -10]:
        binary_tree.insert(i)

    binary_tree = BinaryTree()
    binary_tree.insert(100)
    node = Node(5)
    binary_tree.root.links[0] = node
    node = Node(80)
    binary_tree.root.links[1] = node
    node = Node(60)
    binary_tree.root.links[1].links[1] = node
    node = Node(70)
    binary_tree.root.links[1].links[0] = node
    node = Node(5)
    binary_tree.root.links[1].links[0].links[0] = node
    node = Node(95)
    binary_tree.root.links[1].links[0].links[1] = node
    node = Node(98)
    binary_tree.root.links[1].links[0].links[1].links[1] = node
    node = Node(10)
    binary_tree.root.links[1].links[1].links[0] = node
    node = Node(6)
    binary_tree.root.links[1].links[1].links[0].links[0] = node
    node = Node(50)
    binary_tree.root.links[1].links[1].links[1] = node
    node = Node(3)
    binary_tree.root.links[0].links[0] = node
    node = Node(8)
    binary_tree.root.links[0].links[1] = node
    node = Node(2)
    binary_tree.root.links[0].links[0].links[0] = node
    node = Node(4)
    binary_tree.root.links[0].links[0].links[1] = node
    node = Node(7)
    binary_tree.root.links[0].links[1].links[0] = node
    node = Node(9)
    binary_tree.root.links[0].links[1].links[1] = node
    node = Node(1)
    binary_tree.root.links[0].links[0].links[0].links[0] = node
    node = Node(15)

    binary_tree.root.links[0].links[1].links[1].links[1] = node
    binary_tree.print_tree()
    #print(binary_tree.count_universal_subtrees())
    print(binary_tree.find_bstree())