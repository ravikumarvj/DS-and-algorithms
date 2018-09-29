### COPIED ###
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
    while start <= end:  # Note: <=
        mid = (start + end) // 2
        if arr[mid] == key:
            return True
        if key < arr[mid]:  # Double check conditions
            end = mid - 1
        else:
            start = mid + 1

    return False


def find_min(arr):
    start = 0
    end = len(arr) - 1

    if arr[start] <= arr[end]:  # use <= for single element array. Take care of 0 element array
        return arr[start]

    while start != end - 1:
        mid = (start + end)//2
        if arr[start] < arr[mid]:
            start = mid
        else:
            end = mid
    return arr[end]


def find_offset(arr):
    if arr[0] < arr[-1]:
        return 0

    start = 0
    end = len(arr) - 1

    while start != end - 1:  # when start == end -1, we have found the problem place
        mid = (start + end) //2
        if arr[mid] <= arr[end]:
            end = mid
        else:
            start = mid

    return end

def bin_sear_rotated(arr, num):
    offset = find_offset(arr)
    if num >= arr[0]:  # dont forget >=, because you may be searching arr[0]
        return b_search(arr[0:offset], num)
    else:
        return b_search(arr[offset:], num)




if __name__ == '__main__':
    #    arr = [3, 5, 8, 19, 28, 37, 45, 56, 58, 60, 67, 74, 76, 82, 86, 90, 95]
    #    for i in [6, 1, 100, 3, 95, 56, 58, 60, 59, 57]:
    #        b_search(arr, i)
    # arr = [300, 400, 500, 600, 50, 60, 70]
    arr = [100, 110, 125, 126, 3, 5, 8, 19, 28, 37, 45, 56, 58, 60, 67, 74, 76, 82, 86, 90, 95]
    for i in [6, 1, 100, 3, 95, 56, 58, 60, 59, 57, 125]:
        print(bin_sear_rotated(arr, i), i)
    print(find_min(arr))

