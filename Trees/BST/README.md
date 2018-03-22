
Binary-Search-Tree
Concept
A BST is a binary tree which additionally satisfies the binary search tree property, which states that the key in each node must be greater than or equal to any key stored in the left sub-tree, and less than any key stored in the right sub-tree. If allowing duplicate key, the insertion rule should be that, if you find a key less than or equal to the current key, insert on left. Otherwise insert on right.

The height of a tree (or subtree because trees are recursive) is the number of nodes from the root to a leaf, not including the root. Sometimes you see the height including the root as well. Either way is correct as long as it's consistently used.

On average, binary search trees with n nodes have O (log n) height. However, in the worst case, binary search trees can have O (n) height, when the unbalanced tree resembles a linked list. Insertion and search requires time proportional to the height of the tree in the worst case, which is O(log n) time in the average case over all trees, but O(n) time in the worst case.

In case of deletion, there are three possible cases to consider:
•	Deleting a node with no children: simply remove the node from the tree.
•	Deleting a node with one child: remove the node and replace it with its child.
•	Deleting a node with two children: call the node to be deleted D. Do not delete D. Instead, choose either its in-order predecessor node or its in-order successor node as replacement node E. Copy the user values of E to D. If E does not have a child simply remove E from its previous parent G. If E has a child, say F, it is a right child. Replace E with F at E's parent.
As with all binary trees, a node's in-order successor is its right subtree's left-most child, and a node's in-order predecessor is the left subtree's right-most child. In either case, this node will have only one or no child at all. Delete it according to one of the two simpler cases above.

The first thing we need is a class for a node. It's also convenient to treat a tree as a whole, so we'll use a second class for the tree:

class Node:
    def __init__(self, data):
        self.data = data
        self.links = [None, None] 
        # left(0 or False)child and right(1 or True) child


class BSTree:
    def __init__(self):
        self.root = None

The only confusing part should be the link-list. We could have used two pointers called left and right, but as the operations on a binary search tree are symmetric, by using an array and a boolean value as the index for that array, we can avoid unnecessary repetition of code with only a minor increase in complexity. 

