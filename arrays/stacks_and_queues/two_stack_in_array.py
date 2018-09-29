### COPIED ###  Verified
class StackFull(Exception):
    pass

class StackEmpty(Exception):
    pass


class TwoStack:
    def __init__(self, N):
        self.array = [0] * N  # array of size N
        self.top_one = 0      # top pointer of first stack
        self.top_two = N - 1  # Top pointer of second stack
        self.size = N

    def push(self, val, stack = 1):
        if self.top_one > self.top_two:  # top_one and top_two may point to same index. Consider stack of size 1
            raise StackFull
        # Below check is redundant as first one will take care of it
        # if self.top_one >= self.size or self.top_two < 0:
        #    raise StackFull

        if stack == 1:
            self.array[self.top_one] = val
            self.top_one += 1
        else:
            self.array[self.top_two] = val
            self.top_two -= 1

    def pop(self, stack = 1):
        if stack == 1:
            if self.top_one <= 0:
                raise StackEmpty
            self.top_one -= 1
            return self.array[self.top_one]
        else:
            if self.top_two >= (self.size - 1):
                raise StackEmpty
            self.top_two += 1
            return self.array[self.top_two]

    def len(self, stack = 1):  # __len__ will take only the object as arg. second arg is not allowed.
        if stack == 1:
            return self.top_one
        else:
            return (self.size - 1) - self.top_two  # Not self.size - self.top_two

    def __len__(self):
        return self.len(1) + self.len(2)

if __name__ == '__main__':
    stacks = TwoStack(10)
    stacks.push(1.1)
    stacks.push(2.2, 1)
    stacks.push(1, 2)
    stacks.push(10, 2)
    stacks.push(6, 2)
    stacks.push(5.5)
    print(stacks.pop(2), stacks.pop(2))
    stacks.push(6.6)
    stacks.push(6.8)
    stacks.push(7, 2)
    stacks.push(99.1, 1)
    stacks.push(0.1, 1)
    stacks.push(3.0)
    print(stacks.pop(2))
    # stacks.push(3.2)
    print(len(stacks))
    print(stacks.len(1), stacks.len(2))
    print(stacks.pop(2))
    print(stacks.pop(1))
    print(stacks.len(1), stacks.len(2), len(stacks))