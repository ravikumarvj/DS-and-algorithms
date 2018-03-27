class Node:
    def __init__(self, data):
        self.data = data
        # left and right child-pointers
        self.links = [None, None]


# Bst is a binary search tree class, which allows duplicates
class Bst:
    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root

        while current:
            if current.data == data:
                return True
            side = data > current.data

            current = current.links[side]

        return False

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return True

        current = self.root
        parent = None

        while current:
#           if current.data == data:
#               return False

            side = data > current.data

            parent = current
            current = current.links[side]

        parent.links[side] = Node(data)
        return True


    def _inorder(self, nod):
        if nod:
            self._inorder(nod.links[0])
            print(nod.data, end = ' ')
            self._inorder(nod.links[1])

    def inorder(self):  
        self._inorder(self.root)
        print('\n', '-'*10)     
    
    def _search(self, data, start):
        current = start

        while current:
            if current.data == data:
                return current
            side = data > current.data

            current = current.links[side]

        return None

    def count(self, data):
        ret = 0
        start = self.root

        while True: 
            start = self._search(data, start)
            if start:
                ret += 1
            else:
                return ret
            start = start.links[0]
        return ret

    @staticmethod
    def find_smallest(start):
        while start.links[0]:
            start = start.links[0]

        return start

    @staticmethod
    def _delete_recur(data, start):
        if start is None:
            return None

        if data == start.data:
            if start.links[0] is None and start.links[1] is None:
                return None
            if start.links[0] is None:
                return start.links[1]
            if start.links[1] is None:
                return start.links[0]

            replace = Bst.find_smallest(start.links[1])
            start.data = replace.data
            start.links[1] = Bst._delete_recur(replace.data, start.links[1])
            return start

        side = data > start.data
        start.links[side] = Bst._delete_recur(data, start.links[side])
        return start

    def delete_recur (self, data):
        self.root = Bst._delete_recur(data, self.root)

    @staticmethod
    def _delete(data, start, ancestor, direction):
        current = start
        parent = ancestor
        side = direction

        while current:
            if current.data != data:
                side = data > current.data
                parent = current
                current = current.links[side]
            else:
                break
        else:
            # current is None
            return None

        if current.links[0] is None and current.links[1] is None:
            substitute = None
        elif current.links[0] is None:
            substitute = current.links[1]
        elif current.links[1] is None:
            substitute = current.links[1]

        if current.links[0] and current.links[1]:
            replace = Bst.find_smallest(current.links[1])
            current.data = replace.data
            Bst._delete(replace.data, current.links[1], current, 1)
        else:
            if parent:
                parent.links[side] = substitute
            else:
                self.root = substitute


    @staticmethod
    def find_extreme(current, dir):
        largest = None
        while current:
            largest = current.data
            current = current.links[dir]

        return largest

    def second_element(self, largest = True):
        s_largest = None

        if self.root is None:
            return

        current = self.root

        while current:
            if current.links[largest]:
                s_largest = current.data
                current = current.links[largest]
            else:
                if current.links[not largest]:
                    return self.find_extreme(current.links[not largest], largest)
                else:
                    break
        return s_largest

    '''
    @staticmethod
    def _nth_element(current):
        if not current:
            return None
        Bst._nth_element(current.links[0])
        Bst._nth_element.count -= 1
        if Bst._nth_element.count == 0:
            Bst._nth_element.ret_val = current.data
            return
        Bst._nth_element(current.links[1])



    def nth_element(self, n):
       self._nth_element.count = n
       self._nth_element(self.root)
       print(Bst._nth_element.ret_val)

       # Not- re-entrant
    '''

    def nth_element(self, n):
        from queue import LifoQueue
        stk = LifoQueue()

        if self.root is None:
            return

        stk.put((self.root, False))

        while not stk.empty():
            current, visited = stk.get()

            if visited:
                n -= 1
                if n == 0:
                    return current.data
            else:
                if current.links[1]:
                    stk.put((current.links[1], False))
    
                stk.put((current, True))
                
                if current.links[0]:
                    stk.put((current.links[0], False))

    def delete(self, data):
        self._delete(data, self.root, None, None)

    def lvl_order(self):
        from queue import Queue
        q = Queue()

        if self.root:
            q.put(self.root)

        while not q.empty():
            current = q.get()
            print(current.data, end = ' ')
            if current.links[0]:
                q.put(current.links[0])
            if (current.links[1]):
                q.put(current.links[1])

        print('\n', '-'*10)        


if __name__ == '__main__':
    bstree = Bst()
    l = [52, 50, 20, 80, 34, 2, 16, 98, 56, 46, 56, 98]

    for i in l:
        bstree.insert(i)

    bstree.inorder()
    print()
    print('count of 20: ', bstree.count(20))
    print('count of 80: ', bstree.count(56))

    bstree.inorder()
    bstree.lvl_order()

    print(bstree.second_element(largest = False))
    print('------------')
    print(bstree.nth_element(5))