### COPIED ###   VERIFIED


def partition(array, start, end):
    pivot = array[start]  # take start as the pivot
    i = start + 1
    j = end - 1

    while i <= j:  # i <= j is important. If put i < j, two member array [1, 2] wont enter
        while i < end and array[i] < pivot:
            i += 1  # After this loop, i will be either end or pointing to something >= pivot

        while j > start and array[j] >= pivot:  # Either here, or above should be >= or <=.
            # Otherwise, if i == j (i and j are same index), it will give infinite loop
            j -= 1  # After this, j will be pointing to pivot or something <= pivot

        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1  # Don't forget i and j increments

    # loop ended. Now j is pointing to something <= pivot.
    # And all elements to its right will be > pivot. J could be pointing to start itself
    array[start], array[j] = array[j], array[start]

    return j  # j is the position of pivot


def quick_sort(array, start, end):  # start inclusive, end exclusive
    if end - start < 2:  # array of length 0 or 1 is already sorted
        return

    # partition the array across pivot, such that all elements on left side of pivot are less
    # than pivot and all elements on the right side are greater than pivot
    pivot = partition(array, start, end)

    # Pivot is in place. Recursively sort either sides
    quick_sort(array, start, pivot)
    quick_sort(array, pivot + 1, end)


def sort(array):
    quick_sort(array, 0, len(array))


if __name__ == '__main__':
    array = [100, 100, 75, 100, 50, 15, 125, 50, 150, 15, 50, 130, 15, 45, 50]
    sort(array)
    print(array)