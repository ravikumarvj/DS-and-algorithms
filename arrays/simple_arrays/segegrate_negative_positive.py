### COPIED ###
def segegrate_p_n(array):  # unstable
    start = 0
    end = len(array) - 1

    while start <= end:
        while end >= start and array[end] >= 0:
            end -= 1
        while start >= end and array[start] < 0:
            start += 1
        if start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end += 1

    print(array)


def segegrate_p_n_alt(array):  # Stable (numbers will be in the same order)
    start = 0
    nextp = 0

    while nextp < len(array):
        if array[nextp] < 0:
            array[start], array[nextp] = array[nextp], array[start]
            start += 1
            nextp += 1
        else:
            nextp += 1
    print(array)


array = [9, -3, 5, -2, -8, -6, 1, 3]
segegrate_p_n(array)
array = [-9, -3, 5, -2, 8, -6, 1, -3]
segegrate_p_n_alt(array)