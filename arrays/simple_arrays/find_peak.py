#### COPIED #### VERIFIED
"""
Given an array, find any one peak in the array.
A peak is an element such that it is greater than or equal to both its neighbours.
If the element is a border element(first or last element), then it need to be greater than or
equal to its only neighbour.
"""
def find_peak(array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if (mid - 1 < 0 or array[mid] >= array[mid - 1]) \
                and (mid + 1 >= len(array) or array[mid] >= array[mid + 1]):
            return array[mid], mid
        if mid + 1 >= 0 and array[mid] < array[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    return

array = [1, 1, 1, 1, 1, 1, 2, 3, 3, 3]
array = [3, 2, 1, 2]
print(find_peak(array))