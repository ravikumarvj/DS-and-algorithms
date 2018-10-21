#### COPIED #### VERIFIED
"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""


class Node:  # Node for DLL
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# DLL to insert index from array, based on values from array.
class SpecialDLL:  # Special DLL, because of the sepcial way of insertion
    def __init__(self):
        self.head = None
        self.tail = None

    def del_frm_tail(self):  # Del a node from the end
        if self.tail is None:
            return

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:  # If tail is none, there is no nodes. so make head also none.
            self.head = None

    def del_frm_head(self):  # Del a node from the beginning
        if self.head is None:
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def insert(self, arr, index):  # special insertion
        """
        Special insertion such that the head will have the highest element in ARRAY.
        Discard all the smaller elements from the tail side as they will definitely
        have lesser index values.
        """
        while self.head:
            if arr[index] > arr[self.tail.data]:
                self.del_frm_tail()
            else:
                break

        node = Node(index)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


def print_max(arr, k):
    dll = SpecialDLL()
    n = len(arr)

    # insert k-1 elements first.
    for i in range(k-1):
        dll.insert(arr, i)

    for i in range(k-1, n):
        dll.insert(arr, i)  # insert Kth element onwards and print data from arr
        print(arr[dll.head.data])
        # delete from head only if the window is K. Note that the DLL can have fewer than K nodes
        if dll.head.data == i - (k - 1):
            dll.del_frm_head()

    return 0


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_max(arr, 4)















