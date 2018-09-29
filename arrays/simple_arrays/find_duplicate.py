### COPIED ###  VERIFIED
def find_duplicate(arr, range_max):
    if len(arr) != range_max + 1:
        return None

    start = 1
    end = range_max

    while end > start:
        s_count = 0
        mid = (start + end) // 2
        for i in arr:
            if start <= i <= mid:
                s_count += 1            # If item is between start and mid, increase s_count

        if s_count > mid - start + 1:   # if s_count greater than unique number count between start and mid,
            end = mid
        else:
            start = mid + 1

    # at this point, start will be end, and pointing to out item
    return end


def print_duplicate(arr):
    # go through the list and make the value at index pointed to by current value
    # under consideration to -ve. Use abs(), because we may need to processes -ve values
    for i in arr:
        if arr[abs(i)] < 0:
            print(abs(i))  # i is repeating. Not abs(i)
            break
        arr[abs(i)] = -arr[abs(i)]

    # restore the array
    for i in arr:
        if arr[abs(i)] < 0:
            arr[abs(i)] = -arr[abs(i)]


def find_duplicate_ll(int_list, range_max):

    head = range_max + 1

    # STEP 1: GET INSIDE A CYCLE
    # start at position n+1 and walk n steps to
    # find a position guaranteed to be in a cycle
    cur_position = head
    for _ in range(range_max):
        # cur_position = index + 1
        cur_position = int_list[cur_position - 1]
        # we subtract 1 from the current position to step ahead:
        # the 2nd *position* in a list is *index* 1

    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    remembered_position_in_cycle = cur_position
    current_position_in_cycle    = int_list[cur_position - 1] # 1 step ahead
    cycle_step_count = 1

    while current_position_in_cycle != remembered_position_in_cycle:
        current_position_in_cycle = int_list[current_position_in_cycle - 1]
        cycle_step_count += 1

    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # start two pointers
    #   (1) at position n+1
    #   (2) ahead of position n+1 as many steps as the cycle's length
    pointer_start = head
    pointer_ahead = head
    for _ in range(cycle_step_count):
        pointer_ahead = int_list[pointer_ahead - 1]

    # advance until the pointers are in the same position
    # which is the first node in the cycle
    while pointer_start != pointer_ahead:
        pointer_start = int_list[pointer_start - 1]
        pointer_ahead = int_list[pointer_ahead - 1]

    # since there are multiple values pointing to the first node
    # in the cycle, its position is a duplicate in our list
    return pointer_start

range_max = 16
arr = [3, 5, 4, 1, 6, 2, 8, 7, 9, 10, 16, 15, 14, 12, 13, 11, 15]
print(find_duplicate(arr, range_max))
print_duplicate(arr)
print(find_duplicate_ll(arr, 16))
