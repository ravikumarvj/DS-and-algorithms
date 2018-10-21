### COPIED ###   VERIFIED
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
    if len(array) == 1:
        print('1: ', array)
        return

    start, end = 0, 1   # sliding window. End exclusive
    max_start, max_len = 0, 1  # maximum so far. No need of max_end

    while end < len(array):
        if array[end] > array[end-1]:  # end can be added to the SW
            end += 1
            if end - start > max_len:
                max_start = start
                max_len = end - start
        else:  # New window, starting at end
            start = end
            end += 1

    print(max_len, ':', array[max_start: max_start + max_len])
    return


if __name__ == '__main__':
    array = [1, 1, 1, 2, 3, 4, 4, 4, 4]
    longest_increasing_subarray(array)