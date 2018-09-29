#### COPIED ##### VERIFIED

from k_sorted_array import min_heapify, extract_min, insert_element


def merge_sorted_arrays(*lists):  # lists is a tuple of lists
    ret = []

    k = len(lists)
    # create a heap out of first elements of all the lists.
    # heap elements are of type(num, list_num, next_index)
    heap = [(arr[0], i, 1) for i, arr in enumerate(lists)]
    min_heapify(heap)

    while len(heap):
        small = extract_min(heap)
        ret.append(small[0])

        list_num = small[1]
        next_index = small[2]
        # insert element to heap from the same list (small[1])
        if next_index < len(lists[list_num]):  # next_index < len_of_list
            insert_num = lists[list_num][next_index]
            insert_element(heap, (insert_num, list_num, next_index + 1))

    print(ret)
    return


if __name__ == '__main__':
    a = [10, 20, 30, 40]
    b = [15, 25, 35]
    c = [27, 29, 37, 48, 93]
    d = [32, 33, 34, 35, 56, 100, 105]

    merge_sorted_arrays(a, b, c, d)