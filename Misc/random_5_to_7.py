### COPIED ###
"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
from random import randint
from collections import defaultdict

def rand5():
    return randint(1, 5)

def rand7():
    #    r1 r2 r3 r4 r5
    # r1  1  2  3  4  5
    # r2  6  7  1  2  3
    # r3  4  5  6  7  1
    # r4  2  3  4  5  6
    # r5  7  X  X  X  X
    while True:
        ret = (rand5() - 1)*5 + rand5()-1
        if ret < 21:
            return (ret % 7) + 1

if __name__ == '__main__':
    d = defaultdict(int)
    d2 = defaultdict(int)
    for i in range(7000000):
        d[rand7()] += 1
        d2[randint(1, 7)] += 1
    print(d)
    print(d2)
