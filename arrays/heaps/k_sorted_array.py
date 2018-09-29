#### COPIED #### VERIFIED
def sift_down(array, i, N):
    while i <= (N-2)//2:
        left = i * 2 + 1
        right = i * 2 + 2

        large = i
        if array[left] < array[i]:
            large = left
        if right < N and array[right] < array[large]:
            large = right

        if large == i:
            return
        array[large], array[i] = array[i], array[large]
        i = large


def sift_up(array, index):
    while index > 0:  # if index is 0, nothing to be done
        parent = (index - 1) // 2
        if array[index] >= array[parent]:
            return

        array[index], array[parent] = array[parent], array[index]

        # recursively sift up
        index = parent


def min_heapify(heap):
    N = len(heap)
    for i in range((N-2)//2, -1, -1):
        sift_down(heap, i, N)


def extract_min(heap):
    ret = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    sift_down(heap, 0, len(heap))
    return ret


def insert_element(heap, num):
    heap.append(num)
    sift_up(heap, len(heap) - 1)


def k_sorted_array(array, k):
    # Create a heap out of first K+1 elements
    heap = array[:k+1]
    min_heapify(heap)

    for i in range(len(array)):
        array[i] = extract_min(heap)
        if i + k + 1 < len(array): # Insert one more element to heap
            insert_element(heap, array[i + k + 1])


if __name__ == '__main__':
    arr = [10, 6, 2, 8, 7, 4, 9, 3, 5, 1]
    k = 9
    k_sorted_array(arr, k)
    print(arr)
