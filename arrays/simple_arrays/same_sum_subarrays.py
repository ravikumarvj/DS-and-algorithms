#### COPIED ####
"""
Given two Boolean arrays X and Y, find the length of longest continuous sequence that
starts and ends at same index in both arrays and have same sum. In other words,
find max(j-i+1) for every j &gt;= i where sum of sub-array X[i, j] is equal to
sum of sub-array Y[i, j]
"""


def find_same_sum(arr1, arr2): # assume both arrays to be same length
    temp = [a-b for a, b in zip(arr1, arr2)] # arr1 - arr2
    hashmap = {}
    sum_so_far = 0

    max_start, max_end = -1, -1  # Dont put None as we are using this for comparison

    hashmap[0] = -1
    for i in range(len(temp)):
        sum_so_far += temp[i]
        if sum_so_far in hashmap:
            if i - hashmap[sum_so_far] > max_end - max_start:
                max_end = i
                max_start = hashmap[sum_so_far]
        else:  # update only if it is not in hashmap. we need only the firs occurence of sum_so_far
            hashmap[sum_so_far] = i

    if max_start is not -1:
        return max_start + 1, max_end
    return None

arr1 = [1, 0,  1,  1,  1, 1]
arr2 = [5, 2, -1,  0,  1, 0]
print(find_same_sum(arr1, arr2))
