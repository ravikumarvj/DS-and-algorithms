### COPIED ###
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

def calculate_storage(arr):
    max_end = [0] * len(arr)
    max_val = arr[-1]
    # max_val ==> for each index i, what is the end so far. For arr[-1], it will be 0
    for i in range(len(arr)-2, -1, -1):
        max_end[i] = max_val
        if arr[i] > max_val:
            max_val = arr[i]

    print(max_end)
    max_start = arr[0]  # Tallest seen so far

    capacity = 0
    for i in range(1, len(arr)-1):  # arr[0 and arr[-1] cannot store any water
        if arr[i] < max_start and arr[i] < max_end[i]:
            add = min(max_start, max_end[i]) - arr[i]
            capacity += add

        max_start = max(max_start, arr[i])

    print(capacity)

if __name__ == '__main__':
    arr = [3, 0, 0, 2, 0, 4]
    calculate_storage(arr)