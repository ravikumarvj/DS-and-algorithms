### COPIED ####

def partition(array, left, right):
    if left == right:
        return left
    pivot = array[left]  # May be we can take a randome element beftween left and right
    start = left + 1
    end = right

    while start <= end:
        if array[start] < pivot:
            start += 1
            continue
        if array[end] > pivot:
            end -= 1
            continue
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    array[left], array[start - 1] = array[start - 1], array[left]
    return start - 1


def quick_select_r(array, k, left, right):
    if k < 0 or k >= len(array):
        return None
    index = partition(array, left, right)
    if index == k:
        return array[index]
    if k < index:
        return quick_select_r(array, k, left, index - 1)
    return quick_select_r(array, k, index + 1, right)


def quick_select(array, k): # Find the kth smallest element
    return quick_select_r(array, k-1, 0, len(array) - 1) # k-1 for 0 based index

array = [8, 11, 3, 5, 9, 0, 15, 33, 23, 45, -10]
for i in range(1, len(array) + 1):
    print(quick_select(array, i))

