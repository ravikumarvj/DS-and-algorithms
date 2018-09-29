#### COPIED ####  VERIFIED

"""
Given an array of integers, rearrange the array such that every second element of the array is greater than its left and right elements. Assume no duplicate elements are present in the array
"""
def arrange_alternate_highs(array):
    start = 1
    while start < len(array):
        max_index = start
        if array[start - 1] > array[start]:
            max_index = start - 1
        if start + 1 < len(array) and array[start + 1] > array[max_index]:
            max_index = start + 1

        if max_index != start:
            array[start], array[max_index] = array[max_index], array[start]

        start += 2

    return array

arr = [19, 8, 17, 6, 15, 4, 13, 2, 11, 0]
print(arrange_alternate_highs(arr))