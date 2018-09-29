### COPIED #### VERIFIED
from queue import Queue


class Stack1:  # With one Q
    def __init__(self):
        self.q1 = Queue()

    def push(self, val):
        self.q1.put(val)

    def pop(self):
        size = self.q1.qsize()
        for _ in range(size - 1):
            self.q1.put(self.q1.get())
        return self.q1.get()

    def is_empty(self):
        return self.q1.empty()


class Stack2:  # With 2 queues
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        self.q2.put(val)

        while not self.q1.empty():
            self.q2.put(self.q1.get())
        '''
        while not self.q2.empty():
            self.q1.put(self.q2.get())
        '''
        # Rather than doing the above, just swap the Q names
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.get()

    def is_empty(self):
        return self.q1.empty()


if __name__ == '__main__':
    stk = Stack2()

    for i in range(10, 15):
        stk.push(i)
    print(stk.pop())
    stk.push(45)

    while not stk.is_empty():
        print(stk.pop())
