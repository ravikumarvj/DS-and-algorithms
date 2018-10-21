### COPIED  ####  VERIFIED
"""
You are given a Double LinkList with one pointer of each node pointing to the next node just like in a single link list.
The second pointer however CAN point to any node in the list and not just the previous node. Now write a program in O(n)
time to duplicate this list. That is, write a program which will create a copy of this list.
"""

class Node:
    def __init__(self, data=None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class Dll:
    def __init__(self):
        self.head = None
        self.tail = None


def print_dll(dll):
    node = dll.head

    while node:
        print(node.data, end = ' ')
        if node.next:
            print('next = ', node.next.data, end=' ')
        if node.prev:
            print('prev = ', node.prev.data, end=' ')
        print()
        node = node.next

def clone(dll):
    hash = dict()
    cloned_dll = Dll()

    node = dll.head
    prev = None
    while node:
        temp = Node(node.data)
        if prev is None:
            cloned_dll.head = temp
        else:
            prev.next = temp
        hash[id(node)] = temp
        prev = temp   # Prev != node
        node = node.next

    old_node = dll.head
    new_node = cloned_dll.head
    while old_node:
        if old_node.prev:
            new_node.prev = hash[id(old_node.prev)]
        new_node = new_node.next
        old_node = old_node.next

    if dll.tail:
        cloned_dll.tail = hash[id(dll.tail)]

    return cloned_dll

def clone_2(dll):
    if dll.head is None:
        return

    cloned_dll = Dll()

    node = dll.head
    prev = None
    while node:
        temp = Node(node.data)
        temp.next = node.next
        if dll.tail == node:
            cloned_dll.tail = temp
        node.next = temp
        node = temp.next

    node = dll.head
    while node:
        if node.next and node.prev:
            node.next.prev = node.prev.next
        node = node.next.next

    cloned_dll.head = dll.head.next
    old_node = dll.head
    new_node = cloned_dll.head

    while old_node:
        if old_node.next:
            old_node.next = old_node.next.next
        if new_node.next:
            new_node.next = new_node.next.next
        old_node = old_node.next
        new_node = new_node.next

    print('---------')
    print_dll(dll)
    print('-----------')
    print_dll(cloned_dll)
    print (dll.tail.data, cloned_dll.tail.data)

if __name__ == '__main__':
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = None

    dll = Dll()
    dll.head = one
    dll.tail = five
    five.prev = three
    three.prev = one
    one.prev = two
    six.prev = None
    two.prev = five
    four.prev = three

    print_dll(dll)
    c = clone_2(dll)
    # print_dll(c)