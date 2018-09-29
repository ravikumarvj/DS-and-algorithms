### COPIED ###

def merge(array, start, mid, end):
    temp1 = array[start:mid]  # Extra space O(n)
    # temp2 = array[mid:end]    # temp2 can be avoided by using array itself.

    index = start
    i = 0  # used to go through first partition
    j = mid    # For second partition

    while i < len(temp1) and j < end:
        if temp1[i] < array[j]:
            array[index] = temp1[i]
            i += 1
        else:
            array[index] = array[j]
            j += 1
        index += 1

    while i < len(temp1):
        array[index] = temp1[i]
        index += 1
        i += 1

    # while j < len(array):  These elements are already there
    #    array[index] = array[j]
    #    index += 1
    #    j += 1


def merge_sort(array, start, end):  # start inclusive, end exclusive
    if end - start < 2:  # single element or zero element. Already sorted
        return

    mid = ((end - start) // 2) + start  # Avoid overflow in (start + end)//2

    # Recursively sort
    merge_sort(array, start, mid)
    merge_sort(array, mid, end)

    # merge the halves in to single sorted array
    merge(array, start, mid, end)


def sort(array):
    merge_sort(array, 0, len(array))
    print(array)

if __name__ == '__main__':
    # array = [100, 100, 75, 100, 50, 15, 125, 50, 150, 15, 50, 130, 15, 45, 50]
    array = [5, 4, 3]
    sort(array)