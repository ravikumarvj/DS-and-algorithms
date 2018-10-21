### COPIED ###  VERIFIED
def subarray_greater_sum(arr, value):
    sw_sum, sw_start, sw_end = 0, 0, float('inf')
    sum_so_far, start, end = 0, 0, 0


    for i in range(len(arr)):
        sum_so_far += arr[i]

        # discard any negative sub-array (Kadane's)
        if sum_so_far < 0:  # without this we wont get proper smallest array.
            # Example: [-4, 4, 5] value = 5
            start = i + 1
            sum_so_far = 0

        while sum_so_far >= value: # found . Correct the window to be less than value
            if i - start < sw_end - sw_start:
                sw_start = start
                sw_end = i # inclusive
            sum_so_far -= arr[start]  # Try correcting the window
            start += 1
        # at this point, sum_so_far < value

    print(sw_start, sw_end + 1)
    if sw_end < len(arr):
        print(arr[sw_start:sw_end+1])
    else:
        print('Nothing')

#      0  1  2  3  4  5  6  7
arr = [1, 2, -3, 4, 5, -6, -27, 8, 2, 1, 5, 21, 4]
subarray_greater_sum(arr, 50)