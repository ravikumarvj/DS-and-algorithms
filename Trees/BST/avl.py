'''
 object.__bool__(self)
 Called  to implement truth value testing and the built - in operation bool();
 should return False or True.When this method is not defined, __len__() is called,
 if it is defined, and the object is considered true if its result is nonzero.
 If a class defines neither __len__() nor __bool__(), all its instances are considered true.
 '''

from bst import BSTree


class Node:
    def __init__(self, data):
        self.data = data
        # Default height is 1. Not 0
        self.height = 1  # keep height, instead of balance
        self.links = [None, None]


# Tree, which don't consider duplicates
class AVL(BSTree):
    def __init__(self):
        self.root = None

    @staticmethod
    def _height(start):  # Copied
        return start.height if start else 0

    @staticmethod
    def _update_height(start):  # Copied
        start.height = 1 + max(AVL._height(start.links[0]),
                               AVL._height(start.links[1]))

    @staticmethod
    def _is_balanced(start):  # Copied
        return abs(AVL._height(start.links[0]) - AVL._height(start.links[1])) <= 1

    @staticmethod  # Copied
    def _single_rotate(start, side):  # side = 0 ==> Left rotate
        new_root = start.links[not side]
        start.links[not side] = new_root.links[side]
        new_root.links[side] = start
        AVL._update_height(start)  # Dont forget to update height. Update start first
        AVL._update_height(new_root)

        return new_root

    @staticmethod
    def _double_rotate(start, side):  # side = 1 means right-left rotation
        start.links[side] = AVL._single_rotate(start.links[side], side)  # side rotation
        return AVL._single_rotate(start, not side)

    @staticmethod
    def _insert(start, data):  # copied
        if start is None:
            return Node(data)
        if start.data == data:
            return start  # Always return a node

        side = data > start.data
        start.links[side] = AVL._insert(start.links[side], data)

        # At this point, insertion is done. Update height and balance of node
        AVL._update_height(start)  # Update height
        if AVL._is_balanced(start):
            return start  # Always return node

        # Need balancing
        child = start.links[side]
        in_side = data > child.data  # Check data with child's data

        if in_side == side:
            return AVL._single_rotate(start, not side)
        else:
            return AVL._double_rotate(start, side)  # side - not side rotation

    def insert(self, data):  # Copied
        self.root = self._insert(self.root, data)

    @staticmethod
    def _delete(node, data):  # Copied
        if node is None:
            return None

        if node.data == data:  # found data
            if not any(node.links):  # No child for node
                return None
            if not node.links[0]:
                return node.links[1]
            if not node.links[1]:
                return node.links[0]
            # both children present
            replace = AVL.find_smallest(node.links[1])  # Find a node to replace node
            node.data = replace.data  # replace node's data
            node.links[1] = AVL._delete(node.links[1], replace.data)  # delete replace node, Don't forget assignment
            side = 1  # deletion happened on right side
            # Don't return here as node may need re balancing.
        else:
            side = data > node.data
            node.links[side] = AVL._delete(node.links[side], data)

        # deletion completed
        AVL._update_height(node)
        if AVL._is_balanced(node):  # Already balanced.
            return node

        # Needs balancing. Deletion happened on 'side'. 'not side' should be longer
        l_side = not side # l_side is the longer side
        child = node.links[l_side]  # 'l_side' should still have child
        if AVL._height(child.links[l_side]) >= AVL._height(child.links[not l_side]):  # >=
            # Chained towards same side
            return AVL._single_rotate(node, not l_side)
        else:
            # Zig zag
            return AVL._double_rotate(node, l_side)

    def delete(self, data):  # Copied
        self.root = self._delete(self.root, data)


if __name__ == '__main__':
    avl = AVL()
    count = 0
    # for i in [34, 12, 459, 2, 39, 193, 90, 32, 89, 301, 37, 43]:
    # for i in [34, 12, 459, 2, 39, 193]:
    for i in [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]:
        count += 1
        avl.insert(i)

    avl.print_tree()
    avl.in_order()
    print('')
    for i in [8, 9, 3, 11, 1, 4, 5, 10, 7, 2]:
        avl.delete(i)
    avl.in_order()
    avl.print_tree()