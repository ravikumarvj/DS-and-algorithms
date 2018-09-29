####  COPIED ####
# assume a and b present in array. Find the minimum difference between their indices in array
def find_index_difference(arr, a, b):
    min_a, min_b = None, None
    last_a, last_b = None, None  # last occurences of a and b. We need to keep track of only last occurences
    min_so_far = len(arr)

    for index, num in enumerate(arr):
        if num == a:
            last_a = index
        elif num == b:
            last_b = index
        else:
            continue

        # if last_a and last_b:  # It dont handle 0 index. NBNBNBNBNB. Always be explicit in checks.
        if last_a is not None and last_b is not None:
            if abs(last_a - last_b) < min_so_far:
                min_so_far = abs(last_a - last_b)
                min_a = last_a
                min_b = last_b

    return min_so_far, min_a, min_b

arr = [1, 3, 5, 4, 8, 2, 4, 3, 6, 5, 10]
print(find_index_difference(arr, 1, 10))