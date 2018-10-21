#### COPIED #### VERIFIED
"""
We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""

def merge_and_count(arr, start, mid, end):  # mid element is in second part.
    merge = [0] * (end - start + 1)  # temporary space for merging
    i = start
    j = mid
    inversions = 0

    ins = 0
    while i < mid and j <= end:
        # j is in correct position in arr[mid-end]. i isi in correct position in arr[start-(mid-1)
        # If j goes to arr[start-(mid-1)] number of inversions = mid - i.
        if arr[j] < arr[i]:
            inversions += (mid - i)
            merge[ins] = arr[j]
            j += 1
        else:
            merge[ins] = arr[i]
            i += 1
        ins += 1

    # No inversions in below operations
    if i < mid:
        merge[ins:(end-start+1)] = arr[i:mid] # dont forget :mid as array will include all the elements
    if j <= end:
        merge[ins:(end-start+1)] = arr[j:end+1] # dont forget :end+1

    arr[start:end+1] = merge  # Copy back to array
    return inversions


def count_inversions(arr, start, end): # Both inclusive
    if start >= end:  # one or 0 elements
        return 0

    mid = start + (end - start + 1)//2  # assume start = 0, end = 1. mid = 1. Make calculation like this

    # Divide array in to half and count inversions for either side
    s_i = count_inversions(arr, start, mid - 1)  # 0, 0
    e_i = count_inversions(arr, mid, end)        # 1, 1. Mid should be included here

    # Now while merging, find the inversions between the two sorted array
    # Note that start-mid is on the left and mid-end is on immediate right.
    # So, anything moving from mid-end, before an item in start-end is inversion
    # number of inversion = mid - i
    m_i = merge_and_count(arr, start, mid, end)

    return s_i + e_i + m_i


# TODO: O(N + K)



if __name__ == '__main__':
    arr = [2,3,5,4,1,12, 39, 33, 40, 67, 31, 7]
    print(count_inversions(arr, 0, len(arr) - 1))
    print(arr)