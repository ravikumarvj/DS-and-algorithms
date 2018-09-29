### COPIED ### VERIFIED

from queue import LifoQueue as stack

class Queue:
    def __init__(self):
        self.stack_out = stack()  # Pop stack
        self.stack_in = stack()  # Push stack

    def push(self, val):
        self.stack_in.put(val)  # always push to in stack

    def pop(self):
        if self.stack_out.empty():  # if out stack is empty,
            #  move everything in in stack to out stack one by one
            while not self.stack_in.empty():
                self.stack_out.put(self.stack_in.get())
        # return top most element from out stack
        return self.stack_out.get()

    def is_empty(self):
        return self.stack_out.empty() and self.stack_in.empty()


if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        q.push(i)
    print(q.pop())

    for i in range(10, 14):
        q.push(i)
    print(q.pop())

    print('-' * 10)
    while not q.is_empty():
        print(q.pop(), end = '  ')