#### COPIED #### VERIFIED
"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
find and return the non-duplicated integer.
For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
Do this in O(N) time and O(1) space.

O(N) with O(N) space ==> use hash-table
O(NLogN) with O(1) space ==> use sorting
"""
from math import log2


def update_bit_sums(num, bit_sums):
    while num:
        bit_set = int(log2(num ^ (num & (num-1))))  # Find the last set bit
        num &= (num - 1)
        bit_sums[bit_set] += 1  # add the current bit, to the sum


def find_unique(arr):
    bit_sums = [0] * 64 # array to store bit sums

    for i in arr:
        update_bit_sums(i, bit_sums)

    # For each bit's sum, find mod 3
    for i in range(64):
        bit_sums[i] = bit_sums[i]%3

    # now bit_sums contain the number such that bit_sum[0-63] contains bits 0-63 of result
    ret = 0
    for i in bit_sums[::-1]:
        ret = ret*2 + i

    print(ret)
    return ret

if __name__ == '__main__':
    arr = [2, 6, 6, 3, 4, 0, 19, 19, 0, 13, 3, 4, 19, 4, 3, 0, 101, 6, 2, 13, 2, 13]
    find_unique(arr)
    # This wont work with negative numbers in python, as python have more than 32 leading ones for negative number
    print(bin(-11))  # outputs -0b1011