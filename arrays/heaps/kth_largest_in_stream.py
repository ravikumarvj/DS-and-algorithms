### COPIED ###  VERIFIED
"""
Given an infinite stream of integers, find the k’th largest element at any point of time.
Example:
Input:
stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
k = 3

Output:    {_,   _, 10, 11, 20, 40, 50,  50, ...}
Extra space allowed is O(k).
"""

class MinHeap:
    def __init__(self, k):
        self.heap = [0] * k
        self.length = 0  # current length

    def _sift_down(self, index):
        while index < self.length//2:
            left = index * 2 + 1
            right = index * 2 + 2
            small = index
            if left < self.length and self.heap[left] < self.heap[small]:
                small = left
            if right < self.length and self.heap[right] < self.heap[small]:
                small = right

            if small == index:
                break

            self.heap[small], self.heap[index] = self.heap[index], self.heap[small]
            index = small

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def extract_min(self):
        ret = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.length -= 1
        self._sift_down(0)
        return ret

    def insert(self, val):
        self.heap[self.length] = val
        self._sift_up(self.length)
        self.length += 1

    def extract_and_insert(self, val):
        self.heap[0] = val
        self._sift_down(0)


def print_kth_largest(arr, k):
    heap = MinHeap(k)

    for i in range(k):
        heap.insert(arr[i])

    for i in range(k, len(arr)):
        print(heap.heap[0])
        if arr[i] > heap.heap[0]:
            heap.extract_and_insert(arr[i])

    print(heap.heap[0])


if __name__ == '__main__':
    arr = [10, 20, 11, 70, 50, 40, 100, 5]

    print_kth_largest(arr, 3)