### COPIED ### VERIFIED

def sift_down(array, i, N):
    while i <= (N-2)//2:
        left = i * 2 + 1
        right = i * 2 + 2

        large = i
        if array[left] > array[i]:
            large = left
        if right < N and array[right] > array[large]:
            large = right

        if large == i:
            return
        array[large], array[i] = array[i], array[large]
        i = large


def max_heapify(array):
    N = len(array)
    for i in range((N-2)//2, -1, -1):
        sift_down(array, i, N)
    print(array)


def kth_largest(array, k):
    max_heapify(array)  # Construct MAX heap
    N = len(array)
    for i in range(k-1):  # Move top k-1 objects to the back of array
        array[0], array[N-1-i] = array[N-1-i], array[0]  # always swap with array[0] and not array[i]
        # place array[0] in right position in remaining heap
        sift_down(array, 0, N-1-i)
    return array[0]  # return the current top.


if __name__ == '__main__':
    arr = [5, 18, 24, 13, 4, 101, 76, 53]

    print(kth_largest(arr, 8))
    print(arr)
