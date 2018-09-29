### COPIED ## VERIFIED
class QEmpty(Exception):
    pass


class QFull(Exception):
    pass


class Queue():
    def __init__(self, max_num):
        self.array = [0] * max_num
        self.max = max_num
        self.count = 0
        self.push_ptr = 0
        self.pop_ptr = 0

    def push(self, val):
        if self.count == self.max:
            raise QFull('Queue is full')

        self.array[self.push_ptr] = val
        self.push_ptr = self.incr(self.push_ptr)
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise QEmpty('Queue is empty')
        ret_val = self.array[self.pop_ptr]
        self.pop_ptr = self.incr(self.pop_ptr)
        self.count -= 1
        return ret_val

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.max

    '''
    def decr(self, count):
        return (count - 1) % self.max  # This will work. -1 % 10 = 9
    '''

    def incr(self, count):
        return (count + 1) % self.max

    def peek_elements(self):
        if not self.count:
            return

        temp = self.pop_ptr
        for i in range(self.count):
            print(self.array[temp], end = '  ')
            temp = self.incr(temp)
        print('')
        print('-' * 10)

if __name__ == '__main__':
    que = Queue(6)

    print(que.is_empty(), que.is_full())

    try:
        for i in range(8):
            que.push(i)
    except:
        pass
    print(que.count)
    que.peek_elements()
    print(que.is_empty(), que.is_full())

    try:
        for i in range(10):
            print(que.pop())
    except:
        pass

    print(que.is_empty(), que.is_full())
