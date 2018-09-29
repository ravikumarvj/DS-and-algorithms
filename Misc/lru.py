### COPIED ###
from collections import OrderedDict


class LRUCache_easy():
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_size = 0
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)  # pop out the key. No need to store the value
            self.cache[key] = value
            return

        if self.current_size == self.capacity:
            self.cache.popitem(False)  # False means FIFO. True means LIFO
        else:
            self.current_size += 1
        self.cache[key] = value

        return

class Node:  # DLL Node
    def __init__(self, key, val):
        self.key = key  # Key
        self.val = val  # Value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity  # Max number of caches
        self.head = Node(None, None)  # Head of DLL
        self.tail = self.head  # Tail of DLL

        for _ in range(self.capacity - 1):  # pre-create the DLL
            node = Node(None, None)
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.hash_table = {}  # hash table for quick lookup

    def insert_node_at_head(self, node):  # util function for insert at head
        node.next = self.head
        self.head.prev = node
        self.head = node
        if self.tail == None:  # case arise when only one node in DLL
            self.tail = node

    def get(self, key):
        if key in self.hash_table:  # Look up dict to get node
            ret_node = self.hash_table[key]

            # If already at head position, no need to re-insert
            if ret_node == self.head:
                return ret_node.val

            # Remove from current position and add at head
            if self.tail == ret_node:
                self.tail = ret_node.prev

            if ret_node.prev:
                ret_node.prev.next = ret_node.next
            if ret_node.next:
                ret_node.next.prev = ret_node.prev

            ret_node.next = None
            ret_node.prev = None

            # removal complete. Add it at head
            self.insert_node_at_head(ret_node)

            return ret_node.val

        return -1

    def put(self, key, value):

        # Changing value of existing key
        if key in self.hash_table:
            node = self.hash_table[key]
            node.val = value
            self.get(key)  # Touch it, so that it comes to head
            return

        # remove the LRU node
        del_node = self.tail
        if del_node.key in self.hash_table:
            self.hash_table.pop(del_node.key)

        if del_node.prev:
            self.tail = del_node.prev
            del_node.prev.next = None
            del_node.prev = None

        insert_node = del_node
        insert_node.key = key
        insert_node.val = value
        self.hash_table[key] = insert_node

        self.insert_node_at_head(insert_node)


if __name__ == '__main__':
    capacity = 3
    lru = LRUCache_easy(capacity)
    print(lru.put(2, 2))
    print(lru.put(3, 3))
    print(lru.get(2))
    print(lru.put(4, 4))
    print(lru.put(5, 5))
    print(lru.get(2))
    print(lru.get(3))