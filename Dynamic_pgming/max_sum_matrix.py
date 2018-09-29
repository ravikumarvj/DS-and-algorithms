#### COPIED #### VERIFIED
"""
Given a 2D array, find the maximum sum subarray in it.
"""

def kadanes(array, m):
    sum_so_far = 0
    start, end = 0, 0
    max_sum, max_start, max_end = 0, 0, 0

    for i in range(m):
        sum_so_far += array[i]
        if sum_so_far < 0:
            sum_so_far = 0
            start = i + 1
        elif sum_so_far > max_sum:
            max_start = start
            max_sum = sum_so_far
            max_end = i  # inclusive

    print(max_sum, max_start, max_end)
    return max_sum, max_start, max_end


def find_max_sum(arr, m, n):  # m rows and n colomns
    max_sum = 0
    max_left, max_right = 0, 0
    max_up, max_down = 0, 0

    for left in range(n):
        temp = [0] * m
        for right in range(left, n):
            for i in range(m):
                temp[i] += arr[i][right]
            sum_so_far, sum_start, sum_end = kadanes(temp, m)

            if sum_so_far > max_sum:
                max_up = sum_start
                max_down = sum_end
                max_left = left
                max_right = right
                max_sum = sum_so_far

    print(max_sum, max_left, max_right, max_up, max_down)
    return max_sum

arr = [[ 1,  2, -1, -4, -20],
       [-8, -3,  4,  2,   1],
       [ 3,  8, 10,  1,   3],
       [-4, -1,  1,  7,  -6]]

find_max_sum(arr, 4, 5)