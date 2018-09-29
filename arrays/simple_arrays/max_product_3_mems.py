"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
"""

def find_max_3_mems(array):
    smallest_1 = float('inf')  # Always initialize to inf or -inf
    smallest_2 = float('inf')

    biggest_1 = -float('inf')
    biggest_3 = -float('inf')
    biggest_2 = -float('inf')

    for i in array:
        if i > biggest_1:
            biggest_1, biggest_2, biggest_3 = i, biggest_1, biggest_2
        elif i > biggest_2:
            biggest_2, biggest_3 = i, biggest_2
        elif i > biggest_3:
            biggest_3 = i

        # Dont put elif here.
        if i < smallest_1:
            smallest_1, smallest_2 = i, smallest_1
        elif i < smallest_2:
            smallest_2 = i

    # Dont assume that biggest_1 will abways be positive. If it is negative, below is wrong
    # If all are negative, we have to return smallest magnitude negative number.
    # return biggest_1 * max(smallest_1 * smallest_2, biggest_2 * biggest_3)
    return max(biggest_1 * smallest_1 * smallest_2, biggest_1 * biggest_2 * biggest_3)


array = [-10, -3, -5, -6, -20]
print(find_max_3_mems(array))