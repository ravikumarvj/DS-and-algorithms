#### COPIED ####  VERIFIED
"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array
so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def arrange(arr):
    # R < G < B
    r_ptr = 0
    b_ptr = len(arr) - 1
    start = 0

    while start <= b_ptr:  # Only one traversal
        if arr[start] == 'R':
            arr[start], arr[r_ptr] = arr[r_ptr], arr[start]
            start += 1
            r_ptr += 1
        elif arr[start] == 'B': # Swap to end
            arr[start], arr[b_ptr] = arr[b_ptr], arr[start]
            # Decrement only b_ptr, because the swapped in value could be 'R'. Means keep start as is for next loop
            # In above if condition (arr[start] == 'R', swapped in value will never be 'B', because
            # 'start' already covered that possibility
            b_ptr -= 1
        else:  # arr[start] == 'G'. Let it be there
            start += 1

    return arr

# Partition such that all elements within [0:2) will come first, all between [2:8) next and finally
# all the elements between [8:10)
def partition(arr, mid_start, mid_end): # mid_start inclusive, mid_end exlusive
    f_ptr = 0
    e_ptr = len(arr) - 1
    start = 0

    while start <= e_ptr:
        if arr[start] < mid_start:
            arr[start], arr[f_ptr] = arr[f_ptr], arr[start]
            start += 1
            f_ptr += 1
        elif arr[start] >= mid_end:  # mid_end is not included in MID elements
            arr[start], arr[e_ptr] = arr[e_ptr], arr[start]
            e_ptr -= 1
        else:
            start += 1

    return arr

if __name__ == '__main__':
    arr = ['B', 'R', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'R', 'G']
    print(arrange(arr))

    arr = [1, 2, 3, 4, 5.8, 1.7, 7, 8.4, 9, 2.3, 5, 7.3, 2, 4, 6, 9, 0, 0.9, 6, 9]
    print(partition(arr, 2, 8))