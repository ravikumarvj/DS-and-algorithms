#### COPIED ###  VERIFIED
"""
Given a set of positive integers S, partition the set S into two subsets S1, S2 such that
the difference between the sum of elements in S1 and the sum of elements in S2 is minimized
"""


def min_diff_partion(array, n, total, memo):
    if n == 0:  # No elements left, return total
        return total

    if n in memo and total in memo[n]: # memoization
        return memo[n][total]

    if 0 == total:  # total is 0. This is as close total can come to 0
        return 0

    # Make total close to 0 by either including ot excludint array[n-1]
    ret1 = min_diff_partion(array, n-1, total-array[n-1], memo)
    ret2 = min_diff_partion(array, n-1, total, memo)

    # find number from total (so far), ret1 and ret2, which is closes to zero
    minim = ret1 if abs(ret1) < abs(ret2) else ret2
    minim = minim if abs(minim) < abs(total) else total

    memo[n][sum] = minim
    return memo[n][sum]


from collections import defaultdict
def find_min_diff_partition(array):
    total = sum(array)
    half = total // 2  # get half.
    memo = defaultdict(dict)

    # try to make half close to 0. Return value is how much close we can bring half to zero
    ret = min_diff_partion(array, len(array), half, memo)
    sum1 = half - ret
    sum2 = total - sum1

    return abs(sum1 - sum2)


def min_diff_partition_two(array, n, sum1, sum2, memo):  # initially sum1 and sum2 are 0
    if n == 0:
        return abs(sum1-sum2)

    if (sum1, sum2) in memo:
        return memo[(sum1, sum2)]

    # add current value to sum1
    ret1 = min_diff_partition_two(array, n-1, sum1+array[n-1], sum2, memo)
    # or to sum2 and finf the minimum of returns
    ret2 = min_diff_partition_two(array, n-1, sum1, sum2+array[n-1], memo)

    memo[(sum1, sum2)] = ret1 if abs(ret1) < abs(ret2) else ret2
    return memo[(sum1, sum2)]

def find_min_diff_two(array):
    memo = dict()
    # start both sum1 and sum2 from 0
    return min_diff_partition_two(array, len(array), 0, 0, memo)


array = [-103, 29, -25, 30, 20, 210]
print(find_min_diff_partition(array))
print(find_min_diff_two(array))