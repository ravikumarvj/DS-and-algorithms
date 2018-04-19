# Given an array of integers, we have to find two elements whose XOR is maximum.
class Node:  # Copied
    def __init__(self, digit, num = None):
        self.key = digit          # current bit (only 0 or 1)
        self.num = num            # Data associated with node
        self.children = [None, None]  # 0 or 1


class XorTrie:  # Copied
    INT_MAX_LEN =8  # This should be the max bits in a integer.
                     # If integers are of 32 bits, this should 32

    def __init__(self, array=None):
        self.root = Node('*')
        self.array = []  # It is necessary for max_xor, iff we are calculating MAX_XOR after adding all elements
        if array:
            for i in array:
                self.insert(i)

    def insert(self, num):
        self.array.append(num)  # only for max_xor, iff we are calculating MAX_XOR after adding all elements
        node = self.root
        for i in range(XorTrie.INT_MAX_LEN - 1, -1, -1):  # range '31 - 0'
            digit = (num >> i) & 1  # Get the ith bit
            # digit = bool(num & (1 << i)) # ==> also will work, as this give True(1) or False(0)

            if node.children[digit] is None:
                node.children[digit] = Node(digit)
            node = node.children[digit]
        node.num = num

    def find_min_xor(self, num):  # find min_xor for the given 'num'
        node = self.root
        for i in range(XorTrie.INT_MAX_LEN - 1, -1, -1):
            digit = (num >> i) & 1
            if node.children[digit]:  # If same digit exist in trie, follow that path as same ^ same = 0
                node = node.children[digit]
            else:
                node = node.children[not digit]  # else follow, whatever path available.
                # Make sure we have atleast one element in trie, before calling this method.

        x_num = node.num  # we have reached a terminal node. All 'num' is 32 bits long
        return x_num ^ num, num, x_num

    def find_max_xor(self):
        max_xor = 0  # max_xor can be initialized as 0, unlike min_xor
        for num in self.array:  # go through all the numbers one by one and find max_xor for each
            node = self.root

            for i in range(XorTrie.INT_MAX_LEN - 1, -1, -1):
                digit = (num >> i) & 1
                if node.children[not digit]:  # Follow the path where bits are different
                    node = node.children[not digit]
                else:
                    node = node.children[digit]

            x_num = node.num
            if num ^ x_num > max_xor:
                max_xor = num ^ x_num
                a, b = num, x_num

        print(max_xor, a, b)


def find_min_xor(array):  # Copied
    array.sort()

    if len(array) < 2: return None, None, None  # Corner case
    min_xor = array[0] ^ array[1]  # initialize min xor.

    a, b = array[0], array[1]  # corner case, when len(array = 2
    for i in range(1, len(array) - 1): # Not len(array), because i + 1 should be valid
        if array[i] ^ array[i + 1] < min_xor:
            min_xor = array[i] ^ array[i + 1]
            a, b = array[i], array[i + 1]

    print(min_xor, a, b)

if __name__ == '__main__':
    array = [19, 22, 99, 87, 80, 94, 11, 38, 56, 25]

    tri = XorTrie(array[:2])  # create trie with 1 element

    min_xor = array[0] ^ array[1]  # initialise min_xor as XOR of first two elements
    val1, val2 = array[0], array[1]

    for i in array[2:]:  # for each new element
        ret, a, b = tri.find_min_xor(i)  # find the min xor of elements added to trie so far
        if ret < min_xor:
            min_xor = ret
            val1, val2 = a, b
        tri.insert(i)  # insert this element

    print(min_xor, val1, val2)

    # For MAX_XOR, we can add elements one by one like MIN_XOR and check.
    # It will work also when elements are already added to trie.
    # If elements are already added to trie, MIN_XOR will not work because
    # it will try to calculate A ^ A ( = 0) and always return that.
    tri.find_max_xor()


    find_min_xor(array)