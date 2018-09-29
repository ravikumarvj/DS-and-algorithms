### COPIED ###  VERIFIED
"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.

Note: Idea is to store local maximas (Maximums so far)
"""

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

class MaxMinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        max_val = self.max_stack.peek()
        min_val = self.min_stack.peek()
        if min_val is None or item < min_val:
                self.min_stack.push(item)

        if max_val is None or item > max_val:
                self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.min_stack.peek():
            self.min_stack.pop()
        if item == self.max_stack.peek():
            self.max_stack.pop()

        return item

    def peek(self):
        return self.stack.peek()

    def get_max(self):
        return self.max_stack.peek()

    def get_min(self):
        return self.min_stack.peek()

class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item to the top of our stack."""
        self.stack.push(item)

        # If the item is greater than or equal to the last item in maxes_stack,
        # it's the new max! So we'll add it to maxes_stack.
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxes_stack.peek()



class minStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val):
        if self.min_val is None:
            self.min_val = val

        if val < self.min_val:  # New minimum value
            # 2*val - self.min_val is guaranteed to be < val
            self.stack.append(2*val - self.min_val)
            self.min_val = val  # new min_val
        else:
            # No processing needed
            self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
             return None # Or raise exception
        val = self.stack.pop()
        if val > self.min_val:  # No issues
            return val

        # Need processing before returning
        ret_val = self.min_val  # this is the value to be returned
        # update new min_val.  val = 2*ret_val - Old_min_elem
        # old_min_elem = 2*ret_val - val
        self.min_val = 2*ret_val - val
        return ret_val

    def get_min(self):
        if len(self.stack) == 0:
            return None
        return self.min_val


if __name__ == '__main__':
    stk = MaxMinStack()
    for i in [45, 23, 67, 38, 100, 19, 34, 58, 21]:
        stk.push(i)

    # print(stk.get_max())
    # print(stk.get_min())
    # print(stk.max_stack.items)
    # print(stk.min_stack.items)

    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()

    # print(stk.get_max())
    # print(stk.get_min())
    # print(stk.max_stack.items)
    # print(stk.min_stack.items)
    # print(stk.stack.items)
    # print(stk.maxes_stack.items)

    stk = minStack()
    for i in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6]:
        stk.push(i)
        print(stk.get_min())
    print('--------')
    print(stk.stack)
    print(stk.get_min())
    print(stk.pop(), stk.pop())
    print(stk.get_min())
    print(stk.pop(), stk.pop())
    print(stk.get_min())
    print(stk.pop(), stk.pop())
    print(stk.get_min())
    print(stk.pop(), stk.pop())
    print(stk.get_min())
    print(stk.pop(), stk.pop())
    print(stk.get_min())
    print(stk.pop(), stk.pop())
    print(stk.get_min())


