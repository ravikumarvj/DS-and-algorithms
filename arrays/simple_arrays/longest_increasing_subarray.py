### COPIED ###
"""
Longest increasing subarray (contiguous)
Given an array containing n numbers. The problem is to find the length of the longest contiguous subarray such that every element in the subarray is strictly greater than its previous element in the same subarray. Time Complexity should be O(n).

Examples:

Input : arr[] = {5, 6, 3, 5, 7, 8, 9, 1, 2}
Output : 5
The subarray is {3, 5, 7, 8, 9}

Input : arr[] = {12, 13, 1, 5, 4, 7, 8, 10, 10, 11}
Output : 4
The subarray is {4, 7, 8, 10}
"""


def longest_increasing_subarray(array):
    start, end = 0, 0
    if len(array) < 2:
        print(len(array), ':', array)

    max_l, max_s = 0, 0

    while end < len(array):
        # end + 1 check to avoid special case of checking, last (or only) sequence outside the loop as is [0, 1, 2]
        if (end + 1) < len(array) and array[end] < array[end + 1]:
            end += 1
        else:
            length = (end - start) + 1  # + 1, coz, end is included
            if length > max_l:
                max_l = length
                max_s = start
            end += 1
            start = end

    print(max_l, ':', array[max_s: max_s + max_l])

if __name__ == '__main__':
    array = [12, 13, 10]
    longest_increasing_subarray(array)
