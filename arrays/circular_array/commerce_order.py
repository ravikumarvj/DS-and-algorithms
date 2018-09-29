#### COPIED ####  VERIFIED
"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
-	record(order_id): adds the order_id to the log
-	get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class Order:
    def __init__(self, n):
        self.arr = [-1] * n
        self.insert_p = 0  # Never forget 'self.'
        self.n = n

    def record(self, order_id):
        self.arr[self.insert_p] = order_id
        self.insert_p = (self.insert_p + 1) % self.n

    def get_last(self, i):
        ret = self.arr[(self.insert_p + self.n - i) % self.n]
        return ret if ret != -1 else None



if __name__ == '__main__':
    o = Order(5)
    o.record(3)
    o.record(12)
    o.record(1)
    o.record(98)
    o.record(67)
    o.record(100)
    o.record(1234)
    o.record(922)
    o.record(45)
    print(o.get_last(1))
    print(o.get_last(2))
    print(o.get_last(3))
    print(o.get_last(4))
    print(o.get_last(5))