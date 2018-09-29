#### COPIED ###

def partition_array_same_sum(array):
    total = sum(array)
    sum_so_far = 0

    for i in range(len(array)):
        # sum_so_far is sum ro the left of i, not including i
        if total == sum_so_far: # total represent subarray, to right of i, including i
            return i  # partition across i. i comes in second half

        sum_so_far += array[i]
        total -= array[i]

    return None

arr = [13, 1, 2, 5, 2, 3]
print(partition_array_same_sum(arr))