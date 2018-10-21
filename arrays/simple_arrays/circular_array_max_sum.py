### COPIED ###  VERIFIED
def find_max_sum_cir(arr):
    max_start, max_end, max_sum = 0, 0, 0
    sum_so_far, start = 0, 0

    # simple kadane's algorithm
    for i in range(len(arr)):
        sum_so_far += arr[i]
        if sum_so_far <= 0:  # <= so that we print shortest array. For example, [-4, 4, 8] should output [8]
            sum_so_far = 0
            start = i + 1
        elif sum_so_far > max_sum:
            max_sum = sum_so_far
            max_end = i + 1 # Exclusive
            max_start = start

    min_start, min_end, min_sum = 0, 0, 0
    sum_so_far, start = 0, 0

    # negative sum kadane's. Find max arr with negative sume
    for i in range(len(arr)):
        sum_so_far += arr[i]
        if sum_so_far > 0:
            sum_so_far = 0
            start = i + 1
        # 'or' check is to find the longest such subarray
        elif sum_so_far < min_sum or (sum_so_far == min_sum and (i + 1) - start > min_end - min_start):
            min_sum = sum_so_far
            min_end = i + 1 # exclusive
            min_start = start

    # The final result is either the output of simple Kadane's or
    # Total sum - (sum of max_negative subarray). Logic:
    final_sum = max(max_sum, sum(arr) - min_sum)
    print('sum =', final_sum)
    if final_sum == max_sum:
        print(arr[max_start:max_end])
    else:
        print(arr[min_end:] + arr[:min_start])


     # 0   1   2    3  4  5   6  7  8
arr = [4, -4, 4, -4, 4]
find_max_sum_cir(arr)