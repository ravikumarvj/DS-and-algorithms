#### COPIED #### VERIFIED
from queue import LifoQueue
from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        # left and right child-pointers
        self.left = None
        self.right = None

    def __str__(self):
        return self.data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, data):  # Check if given 'data' is in BST
        current = self.root

        while current:
            if current.data == data:
                return True
            if data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def insert(self, data):  # Copied
        if self.root is None:
            # special case, root is None
            self.root = Node(data)
            return True

        current = self.root
        parent = None  # Keep parent pointer for insertion

        while current:
            if current.data == data:  # No duplicates
                 return False

            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        if data > parent.data:
            parent.right = Node(data)
        else:
            parent.left = Node(data)
        return True

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
            BinarySearchTree.structure(node.right, level+1)
            BinarySearchTree.padding('    ', level)
            print(node.data)
            BinarySearchTree.structure(node.left, level + 1)

    def print_tree(self):
        print('-' * 20)
        BinarySearchTree.structure(self.root, 0)
        print('-' * 20)

    # Given a binary search tree, serialize and de-serialize it
    def serialize(self):  # Serialize using pre-order
        members = []
        if self.root is None:
            return ''

        stack = LifoQueue()
        stack.put(self.root)

        while not stack.empty():
            current = stack.get()
            if current.right:
                stack.put(current.right)
            if current.left:
                stack.put(current.left)
            members.append(current.data)

        ret = ','.join([str(i) for i in members])
        return ret

    def deserialize(self, string):
        if len(string) == 0:
            return

        members = [int(i) for i in string.split(',')]  # Get members as 'int'
        stack = []  # We need peek method to see the data in peek. So used list.

        # MAke the first node as root and append it to stack
        node = Node(members[0])
        self.root = node
        stack.append(node)

        for i in range(1, len(members)):
            node = Node(members[i])

            # IF less that the current stack top, add it as left child of stack top.
            if members[i] < stack[-1].data:
                stack[-1].left = node
                stack.append(node)
            else:
                # Keep on popping till you see something in stack greater than member
                # Add the node as right child of what was popped out last and add it to stack.
                pop = None
                while len(stack):
                    pop = stack[-1]
                    del stack[-1]
                    # check if stack becomes empty or not
                    if len(stack) == 0 or members[i] < stack[-1].data:
                        break

                if pop:
                    pop.right = node
                    stack.append(node)


    # Given a complete binary search tree, serialize and de-serialize it
    def serialize_complete(self):  # Serialize using pre-order
        members = []
        if self.root is None:
            return ''

        q = Queue()
        q.put(self.root)

        while not q.empty():
            current = q.get()
            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)
            members.append(current.data)

        ret = ','.join([str(i) for i in members])
        return ret

    def deserialize_complete(self, string):
        if len(string) == 0:
            return

        members = [int(i) for i in string.split(',')]  # Get members as 'int'
        q = Queue()  # Use same DS used for serialization.

        # MAke the first node as root and append it to stack
        node = Node(members[0])
        self.root = node
        q.put(node)

        i = 1
        while not q.empty():
            current = q.get()
            if i < len(members):
                node1 = Node(members[i])
                i += 1
                current.left = node1
                q.put(node1)
            else:
                break

            if i < len(members):
                node2 = Node(members[i])
                i += 1
                current.right = node2
                q.put(node2)
            else:
                break


    def serialize_full(self):  # Serialize using pre-order
        members = []
        if self.root is None:
            return ''

        q = Queue()
        q.put(self.root)

        while not q.empty():
            current = q.get()

            if current.left is None:  # In full, if left is None, right is also None
                members.append(str(current.data) + 'x')
            else:
                q.put(current.left)
                q.put(current.right)
                members.append(str(current.data))

        ret = ','.join(members)
        return ret

    def deserialize_full(self, string):
        if len(string) == 0:
            return

        members = string.split(',')  # Get members
        q = Queue()  # Use same DS used for serialization.

        # Make the first node as root and append it to stack
        if members[0][-1] == 'x':
            node = Node(members[0][:-1])
            self.root = node
            return
        else:
            node = Node(members[0])
            self.root = node
            q.put(node)

        i = 1
        while not q.empty():
            current = q.get()
            if i < len(members):
                if members[i][-1] == 'x':
                    node1 = Node(int(members[i][:-1]))
                else:
                    node1 = Node(members[i])
                    q.put(node1)
                i += 1
                current.left = node1
            else:
                break

            if i < len(members):
                if members[i][-1] == 'x':
                    node2 = Node(int(members[i][:-1]))
                else:
                    node2 = Node(int(members[i]))
                    q.put(node2)
                i += 1
                current.right = node2
            else:
                break

    def serialize_bt(self):  # Serialize using pre-order
        members = []
        if self.root is None:
            return ''

        q = Queue()
        q.put(self.root)

        while not q.empty():
            current = q.get()
            if current is None:
                members.append(str(None))
                continue

            if current.left is None and current.right is None:
                members.append(str(current.data) + 'x')
            else:
                if current.left is None:
                    q.put(None)
                else:
                    q.put(current.left)
                if current.right is None:
                    q.put(None)
                else:
                    q.put(current.right)
                members.append(str(current.data))

        ret = ','.join(members)
        return ret

    def deserialize_bt(self, string):
        if len(string) == 0:
            return

        members = string.split(',')  # Get members
        q = Queue()  # Use same DS used for serialization.

        # Make the first node as root and append it to stack
        if members[0][-1] == 'x':
            node = Node(members[0][:-1])
            self.root = node
            return
        else:
            node = Node(members[0])
            self.root = node
            q.put(node)

        i = 1
        while not q.empty():
            current = q.get()
            if i < len(members):
                if members[i] == 'None':
                    node1 = None
                elif members[i][-1] == 'x':
                    node1 = Node(int(members[i][:-1]))
                else:
                    node1 = Node(members[i])
                    q.put(node1)
                i += 1
                current.left = node1
            else:
                break

            if i < len(members):
                if members[i] == 'None':
                    node2 = None
                elif members[i][-1] == 'x':
                    node2 = Node(int(members[i][:-1]))
                else:
                    node2 = Node(int(members[i]))
                    q.put(node2)
                i += 1
                current.right = node2
            else:
                break


    def _deepest_node(self, node):  # COPIED
        if node.right is None and node.left is None:
            return node, 1  # leaf at depth 1.

        l_depth = 0
        r_depth = 0

        if node.right:
            r_node, r_depth = self._deepest_node(node.right)
        if node.left:
            l_node, l_depth = self._deepest_node(node.left)

        depth = l_depth if l_depth > r_depth else r_depth  # Find which side have max depth
        ret_node = r_node if depth == r_depth else l_node  # Take node that came from that side

        # increase depth by 1, for current node
        depth += 1

        return ret_node, depth

    def deepest_node(self):  # COPIED
        if self.root is None:
            return
        ret_node, ret_depth = self._deepest_node(self.root)
        print(ret_depth, ret_node.data)

    @staticmethod
    def _invert(node):  # COPIED
        if node is None:
            return

        node.left, node.right = node.right, node.left
        BinarySearchTree._invert(node.left)
        BinarySearchTree._invert(node.right)

    def invert_tree(self):  # COPIED
        if self.root is None:
            return
        BinarySearchTree._invert(self.root)

    def invert_tree_nr(self):  # COPIED
        if self.root is None:
            return

        q = Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            q.put(node.left)
            q.put(node.right)

    def print_zigzag(self):  # COPIED
        q1 = LifoQueue()
        q2 = LifoQueue()

        if self.root is None:
            return

        q1.put(self.root)
        flag = True

        while not q1.empty():
            node = q1.get()
            print(node.data)

            if flag:
                # Going straight. Add left/right, in stack,
                # so taht right will come in top in the next iteration,
                # where we have to go in reverse direction
                if node.left:
                    q2.put(node.left)
                if node.right:
                    q2.put(node.right)
            else:
                # Going in reverse. add right/left
                # so that left will come in top in the next iteration,
                # where we have to go straight
                if node.right:
                    q2.put(node.right)
                if node.left:
                    q2.put(node.left)

            if q1.empty():  # current stack empty
                # change the queues and flags
                q1, q2 = q2, q1
                flag = not flag

    def inorder(self):
        if self.root is None:
            return

        stack = LifoQueue()
        node = self.root

        while node or not stack.empty():
            while node:
                stack.put(node)
                node = node.left  # keep all the left path in stack

            node = stack.get()  # get the top node (left-most child of current subtree)
            print(node.data)

            node = node.right # start with right sub-tree of current node

        return

    # level-order-traversal, with line-break after each level
    def level_order_traversal(self):
        if self.root is None:
            return
        q = Queue()  # Q for level-order (BFS)
        q.put(self.root)
        q.put(None)  # dummy node to understand end of level

        while not q.empty():
            node = q.get()
            if node is None:
                print('')
                print('-------')
                if q.empty():  # Don't forget this, otherwise
                    return     # we will go on infinite loop
                q.put(node) # put level break back again after current level
            else:
                print(node.data, end=' ')
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

        return







def find_root_in_hash(in_hash, value):  # assume no duplicates  # COPIED
    return in_hash[value]

def construct_tree_util(post_arr, in_arr, in_range, post_range, in_hash):  # COPIED
    start_post, end_post = post_range  # end is not included in the range
    if end_post <= start_post:  # ex: If only 1 element at index 0 , then range is (0, 1)
        return None

    # Root is the right most element of post_range
    root = Node(post_arr[end_post - 1])

    # find root's index in in-order array.
    root_index = find_root_in_hash(in_hash, root.data)

    start_in, end_in = in_range
    # Find size of left subtree
    left_length = root_index - start_in
    # Size of right subtree length
    right_length = end_in - root_index - 1 # exclude root itself. #end_in exclusive

    # create new ranges for left subtree
    left_in_range = (start_in, root_index)
    left_post_range = (start_post, start_post + left_length)
    root.left = construct_tree_util(post_arr, in_arr, left_in_range, left_post_range, in_hash)

    # create new ranges for right subtree
    right_in_range = (root_index + 1, end_in)
    right_post_range = (end_post - 1 - right_length, end_post - 1)
    root.right = construct_tree_util(post_arr, in_arr, right_in_range, right_post_range, in_hash)

    return root

def construct_tree(post_arr, in_arr):  # COPIED
    in_hash = {}
    # create reverse index for quick lookup from in_arr. val==>index mapping
    for i, val in enumerate(in_arr):
        in_hash[val] = i # Assume no duplicates in tree.
    # It is difficult to construct a tree with duplicates, for example,
    # consider tree with root:1 left:1 and right:2. In_arr = 1,1,2. post_arr = 1,2,1.
    # When we make a search in in_arr for 1, instead of root 1, we will get left node 1.
    return construct_tree_util(post_arr, in_arr, (0, len(in_arr)), (0, len(post_arr)), in_hash)


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in [45, 80, 4, 20, 5, 10, 2, 120, 100, 200, 201, 12]:
        bst.insert(i)
    # bst.print_tree()

    # serial = bst.serialize()
    # new_bst = BinarySearchTree()
    # new_bst.deserialize(serial)
    # new_bst.print_tree()

    # serial = bst.serialize_complete()
    # new_bst = BinarySearchTree()
    # new_bst.deserialize_complete(serial)
    # new_bst.print_tree()

    # serial = bst.serialize_full()
    # new_bst = BinarySearchTree()
    # new_bst.deserialize_full(serial)
    # new_bst.print_tree()

    # serial = bst.serialize_bt()  # option, cosider as complete binary tree and add 'Null" also in serialzed data
    # print(serial)
    # new_bst = BinarySearchTree()
    # new_bst.deserialize_bt(serial)
    # new_bst.print_tree()
    # bst.deepest_node()

    in_arr = [5, 10, 50, 55, 60, 75, 80, 100, 150, 175, 200, 300]
    post_arr = [5, 10, 55, 60, 80, 75, 50, 175, 150, 300, 200, 100]
    tree = BinarySearchTree()
    tree.root = construct_tree(post_arr, in_arr)
    tree.invert_tree()
    tree.invert_tree_nr()
    BinarySearchTree.print_tree(tree)
    # tree.inorder()
    tree.level_order_traversal()
