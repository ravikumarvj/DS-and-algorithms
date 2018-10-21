### COPIED ###  VERIFIED
# No duplicate key allowed.
class PriorityQueue:
    def __init__(self):
        self.q = []  # List for storing elements
        self.map = {}  # Map to find index of key's fast
        self.length = 0  # Keep track of list size

    def _sift_up(self, index):
        while index > 0:  # if index is 0, nothing to be done
            sub = 1 if index%2 else 2
            parent = (index - sub) // 2
            if self.q[index] >= self.q[parent]:
                return
            # If item is less than parent, swap with parent
            self.q[index], self.q[parent] = self.q[parent], self.q[index]

            # Don't forget to update the map for new positions
            self.map[self.q[index][1]] = index
            self.map[self.q[parent][1]] = parent

            # recursively sift up
            index = parent

    def add_with_priority(self, key, priority):
        self.q.append((priority, key))
        self.map[key] = self.length  # update the map for the key
        self._sift_up(self.length)  # Put the item in proper position
        self.length += 1

    def decrease_priority(self, key, new_priority):
        # assume new_priority is lesser
        if key in self.map:
            index = self.map[key]
            # No need to update map, now as only priority is changed
            self.q[index] = (new_priority, key)
            self._sift_up(index)
        else:
            self.add_with_priority(key, new_priority)

    def _sift_down(self, index):
        while index < self.length:
            left = 2 * index + 1
            right = 2 * index + 2
            small = index  # Start with small as index

            if left < self.length and self.q[left] < self.q[index]:
                small = left
            if right < self.length and self.q[right] <  self.q[small]:
                small = right

            if index == small:
                return

            self.q[small], self.q[index] = self.q[index], self.q[small]
            # Update the map of new locations
            self.map[self.q[index][1]] = index
            self.map[self.q[small][1]] = small
            index = small

    def extract_min(self):
        if self.length == 0:
            return
        ret = self.q[0][1]  # min is at 0'th position
        self.q[0] = self.q[-1]  # Put last element in 0th loc
        # Update map
        self.map[self.q[0][1]] = 0
        del self.map[ret]  # Delete the map for ret
        self.q.pop()  # remove last element
        self.length -= 1
        self._sift_down(0)  # bring down 0th element to correct loc
        return ret


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.add_with_priority('a', 5)
    pq.add_with_priority('b', 8)
    pq.add_with_priority('c', 10)
    pq.add_with_priority('z', 1)
    pq.add_with_priority('d', 5)
    pq.add_with_priority('m', 6)
    pq.add_with_priority('r', 5)
    pq.add_with_priority('p', 8)
    pq.add_with_priority('q', 7)
    pq.decrease_priority('e', 3)
    pq.decrease_priority('f', 2)
    pq.decrease_priority('p', 3)
    pq.decrease_priority('n', 4)
    print(*enumerate(pq.q))
    print(pq.map)
    pq.extract_min()
    pq.extract_min()
    pq.extract_min()
    pq.extract_min()
    pq.decrease_priority('q', 1)
    pq.extract_min()
    print(*enumerate(pq.q))
    print(pq.map)
    pq.extract_min()
    pq.extract_min()
    pq.extract_min()
    pq.extract_min()
    pq.decrease_priority('c', 1)
    pq.extract_min()
    pq.extract_min()
    pq.extract_min()
    pq.extract_min()
    print(*enumerate(pq.q))
    print(pq.map)