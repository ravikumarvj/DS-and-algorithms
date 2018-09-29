import ctypes

class Node:
    def __init__(self, data=None, xor_val = None):
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
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.l.append(self.head)
            return

        prev = 0
        temp = self.head
        print(data, '*')
        # print(id(self.head), Dll._get_obj(id(self.head)))
        while temp.xor_val and temp.xor_val != prev:
            p_temp = temp
            temp = Dll._get_obj(temp.xor_val^prev)
            prev = id(p_temp)

        node = Node(data, id(temp))
        self.l.append(node)  # In python, this is needed to avoid auto-garbage collection of node
        temp.xor_val = prev ^ id(node)

    def get(self, index):
        if self.head is None:
            return None

        temp = self.head
        prev = 0
        index -= 1

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
    print(linked_list.get(14))
    # print(linked_list.start.data)