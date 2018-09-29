#### COPIED ####
from queue import LifoQueue, Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.next_right = None
        self.prev_left = None


# Convert sorted DLL to balanced BST in place. Runtime O(nlogn), Space: O(logn)
def convert_dll_to_bst(dll):  # Start of DLL is passed
    if dll is None or dll.next_right is None:  # single element DLL is BST by default
        return dll

    # Find the middle element of the BST. If DLL is 1,2,3, middle = 2. 1,2,3,4, middle = 3
    middle = dll
    jump = dll
    while jump and jump.next_right:  # O(n)
        middle = middle.next_right
        jump = jump.next_right
        if jump:
            jump = jump.next_right

    # At this point middle will be pointing to the middle element of dll passed
    # Now break the DLL to two halves across middle. Middle will be the root of sub-tree
    first_half = dll
    if middle.prev_left:
        middle.prev_left.next_right = None
    middle.prev_left = None

    second_half = middle.next_right
    if middle.next_right:
        middle.next_right.prev_left = None
    middle.next_right = None

    # create tree recursively
    middle.prev_left = convert_dll_to_bst(first_half)
    middle.next_right = convert_dll_to_bst(second_half)

    # return the root
    return middle


def _convert_dll_to_bst_list(node_list, start, end):  # convert node_list[0...end] to bst
    mid = start + (end - start + 1)//2 # +1 because end is inclusive
    root = node_list[mid]  # middle element is root

    if mid < end: # If there are elements on right: construct right-subtree
        root.next_right = _convert_dll_to_bst_list(node_list, mid+1, end)

    if mid > start: # If there are elements on right: construct left-subtree
        root.prev_left = _convert_dll_to_bst_list(node_list, start, mid-1)

    return root


# Convert sorted DLL to balanced BST in place. Runtime O(n), space: O(n)
def convert_dll_to_bst_list(dll):
    node_list = []
    start = dll
    while start:  # Convert DLL to a list, so that we can easily find the middle element
        node_list.append(start)
        start = start.next_right
        node_list[-1].next_right = None  # break the list
        node_list[-1].prev_left = None   # break the list

    return _convert_dll_to_bst_list(node_list, 0, len(node_list)-1)


def print_bst(bst):
    if bst is None:
        return None
    print_bst(bst.prev_left)
    print(bst.val)
    print_bst(bst.next_right)


def print_max_depth(bst):
    if bst is None:
        return 0

    return 1 + max(print_max_depth(bst.next_right), print_max_depth(bst.prev_left))


def convert_bst_to_dll_r(bst):
    head = None
    tail = None
    dll, _ = _convert_bst_to_dll_r(bst, head, tail)  # You need to pass around tail as insertion is done at tail
    return dll

def _convert_bst_to_dll_r(root, head, tail):
    if root is None:  # If root is none, pass on the head and tail
        return head, tail

    head, tail = _convert_bst_to_dll_r(root.prev_left, head, tail)  # add the left side as DLL

    # insert current root
    if head is None:
        head = root  # updating like this wont reflect across recursion. So we have to return head and tail
        root.prev_left = None # dont make right as None here, or recursion will break.
    else:
        tail.next_right = root
        root.prev_left = tail
    tail = root # tail is always root, whether root is first node or last

    head, tail = _convert_bst_to_dll_r(root.next_right, head, tail)  # add the right side as DLL
    return head, tail


def convert_bst_to_dll(bst):
    #Use stack for in-order traversal
    stack = LifoQueue()
    stack.put((bst, False))  # start with root in stack

    dll_head = None  # Head of dll
    tail = None      # Tail of DLL (for insertions)

    while not stack.empty():
        node, visited = stack.get()

        if visited == True:  # When a node is to be processed, add it to DLL.
            node.next_right = None  # thos should be last node of DLL
            if tail:  # insert at tail
                tail.next_right = node
                node.prev_left = tail
                tail = node
            else:
                dll_head = node
                tail = node
        else:
            if node.next_right:
                stack.put((node.next_right, False))
            stack.put((node, True))
            if node.prev_left:
                stack.put((node.prev_left, False))

    return dll_head


if __name__ == '__main__':
    # dll = None
    # arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # dll = Node(arr[0])
    # start = dll
    # for i in arr[1:]:
    #     node = Node(i)
    #    start.next_right = node
    #    node.prev_left = start
    #    start = node

    # bst = convert_dll_to_bst(dll)

    # print_bst(bst)
    # print('depth: ',print_max_depth(bst))


    dll = None
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    dll = Node(arr[0])
    start = dll
    for i in arr[1:]:
        node = Node(i)
        start.next_right = node
        node.prev_left = start
        start = node
    bst = convert_dll_to_bst_list(dll)
    # print_bst(bst)
    # print('depth: ', print_max_depth(bst))
    # dll = convert_bst_to_dll(bst)

    # print('****')
    dll = convert_bst_to_dll_r(bst)
    start = dll
    while start:
        print(start.val, end=' ')
        start = start.next_right
