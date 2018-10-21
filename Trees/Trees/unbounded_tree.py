#### COPIED #### VERIFIED
import random
from queue import Queue

class Node:
    count = 0
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        Node.count += 1

def generate():
    root = Node(0)
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if random.random() < 0.9:
            node.left = Node(0)
            q.put(node.left)
        if random.random() < 0.9:
            node.right = Node(0)
            q.put(node.right)
        if 0.900000 < random.random() < 0.900001:
            break

    return root

global_count = 100000

class LazyNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right
        self._left_processed = False
        self._right_processed = False

    @property
    def left(self):
        global global_count
        if not self._left_processed:
            if random.random() < global_count/100000:
                self._left = LazyNode(0)
            self._left_processed = True
            global_count -= 1
        return self._left

    @property
    def right(self):
        global global_count
        if not self._right_processed:
            if random.random() < global_count/100000:
                self._right = LazyNode(0)
            self._right_processed = True
            global_count -= 1
        return self._right


def traverse_lazy_tree(root):
    if root is None:
        return
    count = 0

    q = Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        count += 1
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    print(count)



if __name__ =='__main__':
    generate.count = 0
    print(random.random(), random.random())
    # generate()

    # print(Node.count)

    ltree = LazyNode(0)
    traverse_lazy_tree(ltree)