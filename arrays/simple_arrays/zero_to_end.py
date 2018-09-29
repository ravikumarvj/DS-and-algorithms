### COPIED ###
"""
Modify the array by moving all the zeros to the end (right side). The order of other elements doesn’t matter.
Let’s have an example. For array [1, 2, 0, 3, 0, 1, 2], the program can output [1, 2, 3, 1, 2, 0, 0].
"""


def move_zero_to_end(array):  # Copied
    if len(array) == 0:
        return

    start = 0  # always use start and end
    end = len(array) - 1

    while start < end:
        while array[end] == 0 and end > start:  # Skip all trailing zeros
            end -= 1
        while array[start] != 0 and start < end:  # skip all leading non-zeros
            start += 1

        # start is pointing to 0 or end
        # end is pointing to 0 or start
        if start != end:
            array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    print(array)

if __name__ == '__main__':
    array = [0, 9, 0, 4, 7, 0, 6, 8, 1, 0]
    move_zero_to_end(array)