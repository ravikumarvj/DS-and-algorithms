### COPIED ###  VERIFIED

"""
Given an array, find its minimum and maximum value with minimum comparisons
"""

def find_min_max(array, start, end):
    if start == end:  # only one element
        return (array[start], array[end])

    if start + 1 == end:  # only two elements
        if array[start] < array[end]:
            return array[start], array[end]
        else:
            return array[end], array[start]

    mid = start + (end - start) // 2
    min_1, max_1 = find_min_max(array, start, mid)
    min_2, max_2 = find_min_max(array, mid + 1, end)

    return min(min_1, min_2), max(max_1, max_2)


arr = [3, 45, 1, 4325, 32, 49, 45, 79, 30, 11, 346, 97, 84, 72, 98, 83, 81, 61, 64,
       52, 39, 4522, 3424, 4, 43535, 676576, 606, 8383, 220, 334, 567, 234, 34, 56,
       433, 493, 321, 44, 31, 9402, 391, 852, 394, 486, 32112, 454, 43, 432, 39, 7]

print(find_min_max(arr, 0, len(arr) - 1))

