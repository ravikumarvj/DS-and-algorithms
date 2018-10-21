### COPIED ###  VERIFIED

"""
Given an array of numbers in the range 1..100,
return a new array with those same numbers, in sorted order.
There may be repeats in the input array.
If there are, you should include those repeats in your sorted answer.
Useful when we know the range of elements.
"""
from collections import defaultdict

def count_sort(arr, max):
    d = defaultdict(int)
    for i in arr:
        d[i] += 1

    start = 0
    for i in range(max + 1):
        if i in d:
            count = d[i]
            while count:
                arr[start] = i
                start += 1
                count -= 1

    return arr


if __name__ == '__main__':
    arr = [3, 19, 4, 22, 3, 40, 32, 12, 32, 65, 98, 34, 56, 65, 22, 32, 34, 32]
    count_sort(arr, 100)
    print(arr)