#### COPIED #####   VERIFIED
class Et_node:
    # Constructor to create a node
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class ETree:
    def __init__(self):
        self.root = None

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
            ETree.structure(node.right, level+1)
            ETree.padding('    ', level)
            print(node.data)
            ETree.structure(node.left, level + 1)

    def print_tree(self):
        print('-' * 20)
        ETree.structure(self.root, 0)
        print('-' * 20)

def is_operator(i):
    if i == '*' or i == '+' or i == '/' or i == '-':
        return True
    return False

def create_expression_tree(expression):
    tree = ETree()
    stack = []

    for i in expression:
        if is_operator(i):
            node = Et_node(i)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            stack.append(Et_node(i))

    tree.root = stack.pop()
    tree.print_tree()
    return tree


def evaluate_et(tree_node):
    # no null check added here, because we assume operators have both
    # right and left nodes. And number is always leaf node.
    if not is_operator(tree_node.data):
        return tree_node.data

    right = evaluate_et(tree_node.right)
    left = evaluate_et(tree_node.left)

    return str(eval(left+tree_node.data+right))  # convert back to str for subsequent operations


expression = "35*64*1*-"  # how to handle '//' or unary '-'
tree = create_expression_tree(expression)

print(evaluate_et(tree.root))
