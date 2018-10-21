### COPIED ###  VERIFIED
"""
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
"""


def find_number(n):
    i = 19
    while True:
        total = sum(int(x) for x in list(str(i)))
        if total == 10:
            n -= 1
            if n == 0:
                print(i)
                return i
        i += 1


def find_number_9(n):
    i = 19
    while True:
        total = sum(int(x) for x in list(str(i)))
        if total == 10:
            n -= 1
            if n == 0:
                print(i)
                return i
        i += 9


find_number(100)
find_number_9(100)