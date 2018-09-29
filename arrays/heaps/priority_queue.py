### COPIED ###  VERIFIED

# 0 based array used as Q.
# Children: x*2 + 1 and x*2 + 2
# parent: (x-1)//2
# Assume the data to be a tuple as (priority, key, data). Key should be unique
class PriorityQueue:
    # pass min_heap = False for max heap
    def __init__(self, array=None, min_heap=True):
        self.map = {}  # Map to find index of key's fast
        self.length = 0 # Keep track of list size
        if min_heap:
            self.comp = min  # min heap comparison function is min()
        else:
            self.comp = max
        if array is None:
            self.q = []  # List for storing elements
        else:
            self.q = array
            self.length = len(self.q)  # update here as heapify uses length
            i = 0  # update the map
            for _, key, _ in self.q:
                self.map[key] = i
                i += 1
            self.heapify()  # heapify the array

    def heapify(self):
        for i in range((self.length - 2)//2, -1, -1):  # (self.length - 2 //2) inclusive
            self._sift_down(i)  # Push down the tree

    def _sift_down(self, index):  # put the object at index to correct position
        while index < self.length//2:  # Need to do only till half
            left = 2 * index + 1
            right = 2 * index + 2
            change = index

            # Comparison of tuples.
            if left < self.length and self.comp(self.q[left],self.q[index]) == self.q[left]:
                change = left  # if min heap, if min(left, change) is left, change = left
            if right < self.length and self.comp(self.q[right], self.q[change]) == self.q[right]:
                change = right

            if index == change:  # No change in position
                return

            self.q[change], self.q[index] = self.q[index], self.q[change]
            # Update the map of new locations
            self.map[self.q[index][1]] = index
            self.map[self.q[change][1]] = change
            index = change

    def _sift_up(self, index):
        while index > 0:  # if index is 0, nothing to be done
            parent = (index - 1) // 2
            if self.comp(self.q[index], self.q[parent]) == self.q[parent]:
                return

            self.q[index], self.q[parent] = self.q[parent], self.q[index]

            # Don't forget to update the map for new positions
            self.map[self.q[index][1]] = index
            self.map[self.q[parent][1]] = parent

            # recursively sift up
            index = parent

    def add_with_priority(self, priority, key, data = None):
        self.q.append((priority, key, data))
        self.map[key] = self.length  # update the map for the key
        self._sift_up(self.length)  # Put the item in proper position
        self.length += 1

    def change_priority(self, key, new_priority):
        if key in self.map:
            index = self.map[key]
            old_priority = self.q[index][0]
            # No need to update map, now as only priority is changed
            self.q[index] = (new_priority, key, self.q[index][2])

            if (self.comp == min and new_priority < old_priority) or \
                    (self.comp == max and new_priority > old_priority):
                self._sift_up(index)
            else:
                self._sift_down(index)
        else:
            self.add_with_priority(key, new_priority)

    def extract_top(self):
        if self.length == 0:
            return
        ret = self.q[0]  # min/max is at 0'th position
        self.q[0] = self.q[-1]  # Put last element in 0th loc
        # Update map
        self.map[self.q[0][1]] = 0
        del self.map[ret[1]]  # Delete the map for ret
        self.q.pop()  # remove last element
        self.length -= 1
        self._sift_down(0)  # bring down 0th element to correct loc
        return ret

    def print(self):
        print(self.q)


if __name__ == '__main__':
    array = [(4, 15, 15),(2, 16, 16),(3, 17, 17),(4, 18, 18),(1, 19, 19),(3, 20, 20)]
    pq = PriorityQueue(array, min_heap=False)

    pq.add_with_priority(12, 21, 21)
    pq.add_with_priority(2, 22, 22)
    pq.add_with_priority(5, 23, 23)
    pq.add_with_priority(4, 24, 24)
    pq.add_with_priority(3, 25, 25)
    pq.print()
    pq.change_priority(25, 1)
    pq.change_priority(22, 12)
    pq.change_priority(23, 2)
    pq.change_priority(16, 5)
    pq.print()


    while pq.length:
        print(pq.extract_top())
