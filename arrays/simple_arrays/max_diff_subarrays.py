
# from left to right
def kadanes_max_sum_fill_array(array, result):
    sum_so_far = 0
    max_sum = 0

    # result will be filled for left side of 'i', not including 'i'
    for i in range(len(array)-1):
        sum_so_far += array[i]
        if sum_so_far < 0:
            sum_so_far = 0
        else:
            if sum_so_far > max_sum:
                max_sum = sum_so_far
        result[i+1] = max_sum  # Fill in i+1


# from right to left
def kadanes_max_sum_fill_array_reverse(array, result):
    sum_so_far = 0
    max_sum = 0

    # result will be filled for right side of 'i', including 'i'
    for i in range(len(array)-1, -1, -1):
        sum_so_far += array[i]
        if sum_so_far < 0:
            sum_so_far = 0
        else:
            if sum_so_far > max_sum:
                max_sum = sum_so_far
        result[i] = max_sum  # here i is included



def find_max_diff_subarrays(array):
    left_max = [0] * len(array)
    right_max = [0] * len(array)

    kadanes_max_sum_fill_array(array, left_max)  # not including i
    kadanes_max_sum_fill_array_reverse(array, right_max)  # including i

    left_min = [0] * len(array)
    right_min = [0] * len(array)

    # reverse the sign of each element, to find min
    for i in range(len(array)):
        array[i] = -array[i]

    kadanes_max_sum_fill_array(array, left_min)  # not including i
    kadanes_max_sum_fill_array_reverse(array, right_min)  # including i

    # reverse signs of left_min and right_min
    for i in range(len(array)):
        left_min[i] = -left_min[i]
        right_min[i] = - right_min[i]

    max_diff = 0
    for i in range(len(array)):
        max_diff = max(max_diff, left_max[i] - right_min[i],
                       right_max[i] - left_min[i])

    return max_diff


array = [-3, -2, 6, -3, 5, -9, 3, 4, -1, -8, 2 ]
array = [-2, -3, 4, -1, -2, 1, 5, -3]
print(find_max_diff_subarrays(array))