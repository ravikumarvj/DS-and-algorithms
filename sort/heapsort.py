### COPIED ###   VERIFIED


# properly place element in loc in the array[0..end]. Array could be longer than end.
def heapify(array, loc, end):
    while True:
        left = 2 * loc + 1      # left child
        right = 2 * loc + 2     # right child
        move = loc              # element location

        if left < end and array[left] > array[move]:
            move = left

        # move is now greater of node and left child.
        # Use array[move] and not array[loc] as previous if condition might have updated move
        if right < end and array[right] > array[move]:
            move = right
        # move is not greater of node, left and right
        if move == loc:  # no Change. Done
            break

        array[loc], array[move] = array[move], array[loc]
        loc = move


def heap_sort(array):
    end = len(array)

    # start from end-1//2. rest are leaves. No where for them to sift down
    for i in range((end - 1)//2, -1, -1):
        heapify(array, i, end)

    # Swap the max value (array[0]) to end of array and restore heap property.
    for i in range(end - 1, 0, -1):  #
        array[0], array[i] = array[i], array[0]  # largest element so far, moved to i'th location
        heapify(array, 0, i)  # Don't heapify to end. Do only till i


if __name__ == '__main__':
    arr = [20, 150, -35, 20, 100, 20, 100, -35]
    heap_sort(arr)
    print(arr)