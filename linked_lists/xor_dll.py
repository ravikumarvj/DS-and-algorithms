#### COPIED #### VERIFIED
import ctypes

class Node:
    def __init__(self, data=None, xor_val = 0):  # = 0. Not None
        self.data = data
        self.xor_val = xor_val

class Dll:
    def __init__(self):
        self.head = None
        self.tail = None  # DLL needs tail
        # Since we are not stornig any reference to node, it may get garbage-collected.
        self.l = []  #NBNBNB keep track of all nodes to avoid garbage collection

    @staticmethod  ## RAVI NBNBNBNB
    def _get_obj(id):  # Convert id to object
        ret = ctypes.cast(id, ctypes.py_object).value
        return ret

    def add(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            self.tail.xor_val = id(node) ^ self.tail.xor_val
            node.xor_val = id(self.tail)

        self.l.append(node)  # In python, this is needed to avoid auto-garbage collection of node
        self.tail = node

    def get(self, index):  # index starts from 1
        if self.head is None:
            return None

        temp = self.head
        prev = 0
        index -= 1  # index starts from 1

        while index and temp.xor_val and temp.xor_val != prev:
            index -= 1
            p_temp = temp
            temp = Dll._get_obj(temp.xor_val ^ prev)
            prev = id(p_temp)

        print(index, temp)
        if index == 0 and temp:
            return temp.data

        return None

if __name__ == '__main__':
    linked_list = Dll()
    linked_list.add(101)
    linked_list.add(102)
    linked_list.add(103)
    linked_list.add(104)
    linked_list.add(105)
    linked_list.add(106)
    linked_list.add(107)
    linked_list.add(108)
    linked_list.add(109)
    linked_list.add(110)
    linked_list.add(111)
    linked_list.add(112)
    linked_list.add(113)
    print(linked_list.get(1))
    # print(linked_list.start.data)