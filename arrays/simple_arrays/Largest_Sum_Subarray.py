#### Copied ####
def largest_sum(arr):
    sum_so_far = 0
    start_so_far = 0
    max_so_far = 0
    max_start, max_end = 0, 0

    for i in range(len(arr)):
        sum_so_far += arr[i]
        if sum_so_far < 0:
            sum_so_far = 0
            start_so_far = i + 1
        else:
            if max_so_far < sum_so_far:
                max_so_far = sum_so_far
                max_start = start_so_far
                max_end = i+1

    return max_so_far, arr[max_start:max_end]


arr = [-34, 50, -43, 14, 30, -20, 5]
print(largest_sum(arr))