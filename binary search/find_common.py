### COPIED ###

'''
Find The Duplicates
Given two arrays of US social security numbers: Arr1 and Arr2 of lengths n and m respectively, how can you most efficiently compute an array of all persons included on both arrays?
Solve and analyze the complexity for 2 cases:
1. m ≈ n - lengths are approximately the same
'''

import random
import time


def find_common(a1, a2):
    a1.sort()  # n log n
    a2.sort()  # m log m
    l = []
    i, j = 0, 0

    while i < len(a1) and j < len(a2):  # m + n
        if a1[i] == a2[j]:
            l.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1

    # m + n + m log m + n log n
    return l


def b_search(arr, i):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == i:
            return True
        if i < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


def find_common_2(a1, a2):
    # sort smallest and find each element of largest in smallest
    l1, l2 = len(a1), len(a2)
    l = []

    if l1 > l2:
        small = a2
        big = a1
    else:
        small = a1
        big = a2

    small.sort()    # m log m

    le = len(small) - 1
    for i in big:   # n log m
        start = 0
        end = le

        while start <= end:
            if __name__ == '__main__':
                mid = (start + end)//2  # Division takes too much time. So sort both is more efficient
            if small[mid] == i:
                l.append(i)
            if i < small[mid]:
                end = mid - 1
            else:
                start = mid + 1


    # (n + m) log m
    return l

'''
def find_common_2(a1, a2):
    # sort smallest and find each element of largest in smallest
    l1, l2 = len(a1), len(a2)
    l = []

    if l1 > l2:
        small = a2
        big = a1
    else:
        small = a1
        big = a2

    small.sort()    # m log m
    for i in big:   # n log m
        if b_search(small, i):
            l.append(i)

    # (n + m) log m
    return l
'''


if __name__ == '__main__':
    a1 = []
    a2 = []

    for i in range(1000000):
        a1.append(random.randint(1, 25000000))
    for i in range(100):
        a2.append(random.randint(1, 25000000))

    a1 = list(set(a1))
    a2 = list(set(a2))

    t = time.time()
    l = find_common(a1, a2)
    print(len(l), time.time() - t, l)

    t = time.time()
    l = find_common_2(a1, a2)
    print(len(l), time.time() - t, l)

    t = time.time()

    for i in range(1, len(a1)):
        (a1[i - 1] + a1[i - 1])// i
    print(time.time() - t)

