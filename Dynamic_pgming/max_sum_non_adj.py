###### COPIED #######  VERIFIED

def max_sum(array, i, memo, elems):  # i is not 0 based
    # If all negative array, we return 0, meaning dont include any
    # Alternatively, if all negative, parse through once and find highest element
    if i <= 0:  # <= is needed because, we are doing i-2
        return 0

    if memo[i] is not None:
        return memo[i]
    incl = max_sum(array, i-2, memo, elems) + array[i-1]  # i-1 as it is not 0 based
    excl = max_sum(array, i-1, memo, elems)

    memo[i] = max(incl, excl)

    # Put elems[i] only when it is included
    elems[i] = array[i-1] if incl > excl else -1
    return memo[i]


def print_elems(elems, N):
    while N > 0:
        if elems[N] == -1:
            N -= 1
        else:
            print(elems[N], end = ' ')
            N-= 2
    print()

def max_sum_bup(array):
    incl = [-1] * (len(array) + 1)
    n = len(array)
    if n == 1:
        return array[0]
    if n == 2:
        return max(array[0], array[1])

    first = array[0]
    second = max(array[0], array[1])  # Consider a 2 element array

    for i in range(2, n):
        # first could be negative. So, array[i] will be > first + array[i]
        current = max(first + array[i], second, array[i])
        if current == array[i] or (current == first + array[i]):
            incl[i+1] = array[i]
        first = second
        second = current

    print(current)
    print_elems(elems, len(array))
    return current


if __name__ == '__main__':
    array = [-5, -1, 9, 13, 6, 1]
    memo = [None] * (len(array) + 1)
    elems = [0] * (len(array) + 1)
    print(max_sum(array, len(array), memo, elems))
    print_elems(elems, len(array))

    max_sum_bup(array)