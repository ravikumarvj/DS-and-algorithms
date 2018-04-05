'''
1. Find a given number num in a sorted array arr:
arr = [2, 4, 5, 9, 12, 17]
2. If the sorted array arr is shifted left by an unknown offset and you don't have a pre-shifted copy of it, how would you modify your method to find a number in the shifted array?
shiftArr = [9, 12, 17, 2, 4, 5]
Explain and code an efficient solution and analyze its runtime complexity
if num doesn't exist in the array, return -1
'''


def b_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return True
        if arr[mid] > key:  # Double check conditions
            end = mid - 1
        else:
            start = mid + 1

    return False


def find_offset(arr):
    start = 0
    end = len(arr) - 1

    while start != end - 1:
        mid = (start + end) //2
        if arr[mid] <= arr[end]:
            end = mid
        else:
            start = mid

    return end


def b_search_shifted(arr, key):
    if arr[0] > arr[-1]:
        f = find_offset(arr)
        if b_search(arr[:f], key) or b_search(arr[f:], key):
            print('Found', key)
        else:
            print(key, 'Not found')

if __name__ == '__main__':
    #    arr = [3, 5, 8, 19, 28, 37, 45, 56, 58, 60, 67, 74, 76, 82, 86, 90, 95]
    #    for i in [6, 1, 100, 3, 95, 56, 58, 60, 59, 57]:
    #        b_search(arr, i)

    arr = [100, 110, 125, 3, 5, 8, 19, 28, 37, 45, 56, 58, 60, 67, 74, 76, 82, 86, 90, 95]
    for i in [6, 1, 100, 3, 95, 56, 58, 60, 59, 57, 125]:
         b_search_shifted(arr, i)

