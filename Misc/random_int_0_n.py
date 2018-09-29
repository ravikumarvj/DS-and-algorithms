"""
You are given N and an int K[].
The task at hand is to generate a equal probabilistic random number between 0 to N-1 which doesn't exist in K.

N is strictly a integer >= 0. And K.length is < N-1. And 0 <= K[i] <= N-1.
Also assume K is sorted and each element of K is unique.
You are given a function uniformRand(int M) which generates uniform random number in the
range  0 to M-1 And assume this functions's complexity is O(1).

Example:
N = 7
K = {0, 1, 5}
the function should return any random number { 2, 3, 4, 6 } with equal probability.
"""

from random import randint
from collections import defaultdict


def generate_random(n, l):
    s = set(range(n))  # O(n)
    s -= set(l)  # O(n)  Find set difference
    l = list(s)  # O(n). Order does not matter, as long as l is fixed. No need to sort

    def my_random():  # create a function that generates random number
        ra = randint(0, len(l)-1)  # both are inclusive
        return l[ra]
    return my_random  # return random number


rand_n_l = generate_random(7, [0, 1, 5])  # get the random number function
d = defaultdict(int)

for i in range(10000):  # Amortized cost is O(1)
    rand = rand_n_l()
    d[rand] += 1


def generate_random_once(n, l):  # assume l to be sorted
    val = n - len(l)
    if val == 0:
        return

    # generate a random number between 1-val
    r = randint(0, val - 1) + 1
    # Find r'th missing element in l using binary search
    start = 0
    end = len(l) - 1

    while start <= end:
        mid = start + (end - start) // 2   # 2

        missing_start = l[start] - start
        missing_end = l[end] - end
        missing_mid = l[mid] - mid

        # rth missing is before start. Note less than or equal.
        # For example, if number 5 is at index 0, and r is 5, 5th miss is
        # 5-1 = 4  [0, 1, 2, 3, 4]. 2nd miss is 1 = 5-(5-(2-1)) = 5-4=1
        if r <= missing_start:
            # -1 is there here because, we are adding 1 to r
            ret = l[start] - (missing_start - (r-1))
            print(ret)
            return ret

        # rth missing is after end. say, last is 10 at index 5.
        # 10-5 = 5 are missing before 10. For example, 0, 1, 2, 3, 4, 10.
        # 5, 6, 7, 8, and 9 are missing. Now 6th missing is 10 + 6-5 = 11.
        # 7th missing is 10 + (7-5) = 12
        if r > missing_end:
            ret = l[end] + (r-missing_end)
            print(ret)
            return ret

        # missing is between start and end
        if r > missing_mid:
            # Dont do mid + 1. see 0, 1, 2 as start mid and end
            start = mid + 1
        else:
            print(r, missing_mid, 'here')
            end = mid - 1

    print('none')
    return None

d = defaultdict(int)
for j in range(1):
    d[generate_random_once(14, [3, 5, 8, 10, 12])] += 1

generate_random_once(14, [0, 1, 5, 10])
generate_random_once(5, [0, 2, 3, 4])

print(d)
